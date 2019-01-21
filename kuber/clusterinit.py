import re
import os
import paramiko

class SSHclient:

    "This class is for paramiko"
    import paramiko

    def __init__(self,host_ip,port,username,key=None):

        self.username = username
        self.host_ip = host_ip
        self.port = port
        self.key = key
        if self.key is not None:
            self.key = os.path.expanduser(self.key)

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.ssh.connect(username=self.username, key_filename=self.key, hostname=self.host_ip, port = self.port)
            print('connect successfully!!!')
        except:
            print('connection fail...')


    def close(self):

        if self.ssh is not None:
            self.ssh.close()
            self.ssh = None


    def execute(self,command,sudo=False):

        if sudo == True:
            command = "sudo %s"%command
            #print('command executed: ',command)
        stdin, stdout, stderror = self.ssh.exec_command(command, get_pty=True)
        return {
                'out':stdout.read(),
                'error':stderror.read()
               }


def node_join(manager_publicIP_string, manager_privateIP_string,worker_publicIP_list,path_to_pem,ssh_username):
    import os   
    try:
        manager1_ssh = SSHclient(host_ip=manager_publicIP_string, port=22, username=ssh_username, key=path_to_pem)
        command_init = "sudo su -c \'kubeadm init --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=all\'" # required 2 cpu
        command_grant0 = "mkdir -p $HOME/.kube"
        command_grant1 = "sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config"
        command_grant2 = "sudo chown $(id -u):$(id -g) $HOME/.kube/config"
        command_network0 = "sudo sysctl net.bridge.bridge-nf-call-iptables=1" 
        command_network1 = "kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/bc79dd1505b0c8681ece4de4c0d86c5cd2643275/Documentation/kube-flannel.yml"
        command_check = "bash $HOME/kuber/subprocess/check_kube-system.sh 2> /dev/null"
        token = manager1_ssh.execute(command_init)['out'].decode()
        print(token)
        join_token =  re.search('kubeadm join {}:6443 --token .*'.format(manager_privateIP_string) ,token).group(0)
        print('join_token:', join_token)
        manager1_ssh.execute(command_grant0); manager1_ssh.execute(command_grant1); manager1_ssh.execute(command_grant2)
        manager1_ssh.execute(command_network0);manager1_ssh.execute(command_network1)
        time.sleep(10)

        bol = True
        while bol:
            status = manager1_ssh.execute(command_check)['out'].decode()
            print('Print raw status:',repr(status))
            status = status.strip('\r\n')
            print(status)  
            if status == 'wait': continue
            if status == 'proceed':
                bol = False
                break
        print('Ready to join the node...') 
        
        

        workerNumber=1 
        for workerIP in worker_publicIP_list:
           
            worker_ssh = SSHclient(host_ip=workerIP, port=22, username=ssh_username, key=path_to_pem)
            outmessage = worker_ssh.execute('sudo su -c \"{}\"'.format(join_token))['out'].decode()
            workerNumber+=1
            print("worker%s: %s"%(workerNumber, outmessage))
            worker_ssh.close()       
        
        print('2222') 
        nodesMessage = manager1_ssh.execute('kubectl get nodes')['out'].decode()
        networkMessage = manager1_ssh.execute('kubectl get pods --all-namespaces')['out'].decode()
              
        print('############Cluster status###########\n',nodesMessage)
        manager1_ssh.close()
    except:
        print('ssh fail...')



if __name__ == "__main__":
    import time
    import json
    import boto3
    import os
    with open('aws-multiple.json', 'r') as fh:
        json_data = json.load(fh)

    path_to_pem = json_data['manager']['ssh_private_key_path']
    ssh_username = json_data['manager']['ssh_username']


    ec2c = boto3.client('ec2', 'us-west-1')
    reservations = ec2c.describe_instances(
        Filters=[{
            'Name': 'instance-state-name',
            'Values': ['running']}]
    )['Reservations']
    #print(running_instances)
    managers_ip = list()
    managers_private_ips = list()
    workers_ip = list()
    
    for reservation in reservations:
        Tag = reservation['Instances'][0]['Tags'][0]['Value']
        print(Tag)
        if Tag == 'Node-001':
           managers_ip.append(reservation['Instances'][0]['PublicIpAddress'])
           managers_private_ips.append(reservation['Instances'][0]['PrivateIpAddress'])
        if Tag == 'Node-002':
           workers_ip.append(reservation['Instances'][0]['PublicIpAddress'])
        if Tag == 'Node-003':
           workers_ip.append(reservation['Instances'][0]['PublicIpAddress'])

    print('manager_publicIP:',managers_ip)
    print('manager_privateIP:',managers_private_ips)
    print('worker_publicIP:',workers_ip)

    node_join(manager_publicIP_string=managers_ip[0], manager_privateIP_string=managers_private_ips[0] ,worker_publicIP_list=workers_ip, path_to_pem=path_to_pem, ssh_username = ssh_username)

