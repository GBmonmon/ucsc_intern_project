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


def node_join(ec2_ips,path_to_pem,ssh_username):
    try:
        manager_publicIP_string = ec2_ips[0]['public']
        manager_privateIP_string = ec2_ips[0]['private']
        manager1_ssh = SSHclient(host_ip=manager_publicIP_string, port=22, username=ssh_username, key=path_to_pem)
        manager1_ssh.execute("docker swarm leave --force")
        manager1_ssh.execute("docker swarm init --advertise-addr {}".format(manager_privateIP_string))
        manager1_ssh.execute("docker swarm update --autolock false")
        #manager1_ssh.execute("docker swarm init")
        output = manager1_ssh.execute("docker swarm join-token manager")['out'].decode()
        join_token =  re.search('docker swarm join .*' ,output).group(0) 
        print(join_token,'\n')

        
        workerNumber=1
        worker_publicIP_list = [ ec2_ips[1]['public'], ec2_ips[2]['public'] ]
        for workerIP in worker_publicIP_list:
           
            worker_ssh = SSHclient(host_ip=workerIP, port=22, username=ssh_username, key=path_to_pem)
            worker_ssh.execute("docker swarm leave --force")
            outMessage =  worker_ssh.execute(join_token)['out'].decode() 
            worker_ssh.execute('docker swarm update --autolock false')
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
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            },
            {
                'Name':'tag:Name',
                'Values':['ECS Instance - amazon-ecs-cli-setup-ecs-cluster-1']
            }
                
        ]
    )['Reservations']
    #print(running_instances)
    ec2_ips = list()
    for reservation in reservations:
        instances = reservation['Instances']
        for instance in instances:
            ec2_public_ip = instance['PublicIpAddress']
            ec2_private_ip = instance['PrivateIpAddress']
            ec2_ips.append({'public':ec2_public_ip, 'private':ec2_private_ip}) 
    print(ec2_ips)
 
    node_join(ec2_ips=ec2_ips, path_to_pem=path_to_pem, ssh_username = ssh_username)  
