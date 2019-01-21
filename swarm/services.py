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
    Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']}]
)['Reservations']
#print(running_instances)
managers_ip = list()
workers_ip = list()

for reservation in reservations:
    Tag = reservation['Instances'][0]['Tags'][0]['Value']
    print(Tag)
    if Tag == 'Node-001':
       managers_ip.append(reservation['Instances'][0]['PublicIpAddress'])
    if Tag == 'Node-002':
       workers_ip.append(reservation['Instances'][0]['PublicIpAddress'])
    if Tag == 'Node-003':
       workers_ip.append(reservation['Instances'][0]['PublicIpAddress'])

print('manager:',managers_ip)
print('workers:',workers_ip)


manager1_ssh = SSHclient(host_ip=managers_ip[0], port=22, username=ssh_username, key=path_to_pem)

command1 = "docker stack deploy -c /home/{}/swarm/vote-stacks.yml".format(ssh_username) + " webapp"
print(command1)

manager1_ssh.execute(command1)
manager1_ssh.close()

vote_url1 = managers_ip[0]+':5000'
vote_url2 = workers_ip[0]+':5000'
vote_url3 = workers_ip[1]+':5000'
result_url1 = managers_ip[0]+':5001'
result_url2 = workers_ip[0]+':5001'
result_url3 = workers_ip[1]+':5001'
print(""""
#########################################################
# URL
#########################################################
""")
print('Vote site URL:\n'+vote_url1 + '\n' + vote_url2 + '\n' + vote_url3 + '\n\n' )
print('Vote site URL:\n'+result_url1 + '\n' + result_url2 + '\n' + result_url3 )


