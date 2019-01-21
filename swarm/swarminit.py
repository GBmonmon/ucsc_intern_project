import subprocess
import boto3
import subprocess
import os
import paramiko
import re
import json

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
        stdin, stdout, stderror = self.ssh.exec_command(command)
        return {
                'out':stdout.read(),
                'error':stderror.read()
               }


def node_join(manager_publicIP_string, manager_privateIP_string,worker_publicIP_list,path_to_pem,ssh_username):

    try:
        manager1_ssh = SSHclient(host_ip=manager_publicIP_string, port=22, username=ssh_username, key=path_to_pem)
        manager1_ssh.execute("docker swarm leave --force")
        manager1_ssh.execute("docker swarm init --advertise-addr {}".format(manager_privateIP_string))
        output = manager1_ssh.execute("docker swarm join-token worker")['out'].decode()
        join_token =  re.search('docker swarm join .*' ,output).group(0) 
        print(join_token,'\n')

        workerNumber=1
        for workerIP in worker_publicIP_list:
           
            worker_ssh = SSHclient(host_ip=workerIP, port=22, username=ssh_username, key=path_to_pem)
            worker_ssh.execute("docker swarm leave --force")
            outMessage =  worker_ssh.execute(join_token)['out'].decode() 
            worker_ssh.close()
            print('worker{}:'.format(workerNumber),outMessage)
            workerNumber+=1
        manager1_ssh.close()
    except:
        print('ssh fail...')



if __name__ == "__main__":
    import time
    import json
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
        if Tag == 'Node-001':
           managers_ip.append(reservation['Instances'][0]['PublicIpAddress'])
           managers_private_ips.append(reservation['Instances'][0]['PrivateIpAddress'])
        if Tag == 'Node-002':
           workers_ip.append(reservation['Instances'][0]['PublicIpAddress'])
        if Tag == 'Node-003':
           workers_ip.append(reservation['Instances'][0]['PublicIpAddress'])
    node_join(manager_publicIP_string=managers_ip[0], manager_privateIP_string=managers_private_ips[0] ,worker_publicIP_list=workers_ip, path_to_pem=path_to_pem, ssh_username = ssh_username)  
