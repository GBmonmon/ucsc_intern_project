import subprocess
import time
from swarminit import SSHclient
import boto3
import sys
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
            'Name': 'tag:Name',
            'Values':['ECS Instance - amazon-ecs-cli-setup-ecs-cluster-1']
        }
    ]
)['Reservations']
#print(running_instances)
managers_ip = list()
workers_ip = list()

ec2_ips = list()
for reservation in reservations:
    instances = reservation['Instances']
    for instance in instances:
        ec2_public_ip = instance['PublicIpAddress']
        ec2_private_ip = instance['PrivateIpAddress']
        ec2_ips.append({'public':ec2_public_ip, 'private':ec2_private_ip})
print(ec2_ips)

#print('manager:',managers_ip)
#print('workers:',workers_ip)

for ec2_ip in ec2_ips:
    
    publicip = ec2_ip['public']
    manager1_ssh = SSHclient(host_ip=publicip, port=22, username=ssh_username, key=path_to_pem)
    command1 = "docker stack deploy -c /home/{}/ecs-cli/vote-stacks.yml".format(ssh_username) + " webapp"
    print(command1)
    manager1_ssh.execute(command1)
        

manager1_ssh.close()

vote_url1 = ec2_ips[0]['public']+':5000'
vote_url2 = ec2_ips[1]['public']+':5000'
vote_url3 = ec2_ips[2]['public']+':5000'
result_url1 = ec2_ips[0]['public']+':5001'
result_url2 = ec2_ips[1]['public']+':5001'
result_url3 = ec2_ips[2]['public']+':5001'
print(""""
#########################################################
# URL
#########################################################
""")
print('Vote site URL:\n'+vote_url1 + '\n' + vote_url2 + '\n' + vote_url3 + '\n\n' )
print('Vote site URL:\n'+result_url1 + '\n' + result_url2 + '\n' + result_url3 )


