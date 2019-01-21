import subprocess
import boto3
from botocore.exceptions import ClientError
import time
import re
import ast
from subprocess import call
import os
import sys
import json

if __name__ == '__main__':

    with open('aws-multiple.json', 'r') as fh:
        json_data = json.load(fh)
    
    path_to_pem = json_data['manager']['ssh_private_key_path']
    ssh_username = json_data['manager']['ssh_username']





    result = subprocess.run(['./subprocess/runCluster.sh'], stdout=subprocess.PIPE)
    print(result)
    #result = result.stdout
    #result = result.decode()
    #objs = result.replace('\n', ' ').split(' ')
 
    #sg_ids = list()
    #for obj in objs:
    #    if obj.startswith('sg-'):
    #        sg_ids.append(obj)

   
    #subprocess.call('./subprocess/runCluster.sh')
    bol = True
    while bol: 
        client_ec2 = boto3.client('ec2','us-west-1')
        reservations = client_ec2.describe_instances(
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
        time.sleep(4)
        sg_ids = list()
        ec2_ips = list()
        for reservation in reservations:
            instances = reservation['Instances']
            for instance in instances:
                ec2_public_ip = instance['PublicIpAddress']
                ec2_private_ip = instance['PrivateIpAddress']
                ec2_ips.append({'public':ec2_public_ip, 'private':ec2_private_ip})
  
                sg_id = instance['SecurityGroups'][0]['GroupId']               
                sg_ids.append(sg_id)
        if len(ec2_ips) == 3: 
            bol = False
            break
        else:
            print('waiting ec2 to be up and running...')
            print(ec2_ips)
            time.sleep(4)
            continue
    ################ make sure we have needed ports in SG ################ 
    print(ec2_ips)
    print(sg_ids)
    for sg_id in sg_ids:
        # tcp
        for port in [22,80,443,2376,2377,7946,5000,5001,8080]:
            try:
                client_ec2.authorize_security_group_ingress(
                    GroupId = sg_id,
                    IpPermissions = [
                        {
                            'IpProtocol':'tcp',
                            'FromPort': port,
                            'ToPort':port,
                            'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
                        }
                    ]

                )
            except ClientError as e:
                print(e)
                continue
        for port in [7946,4789]:
            try:
                client_ec2.authorize_security_group_ingress(
                    GroupId = sg_id,
                    IpPermissions = [
                        {
                            'IpProtocol':'udp',
                            'FromPort': port,
                            'ToPort':port,
                            'IpRanges':[{'CidrIp':'0.0.0.0/0'}]
                        }
                    ]

                )
            except ClientError as e:
                print(e)
                continue
    time.sleep(4)


    ################ Shared the files with ec2 ################
 
    public_ips = [ i['public'] for i in ec2_ips ]     
    print(public_ips)
    files_to_share = os.getcwd()
    for public_ip in public_ips:
        print('running command: ')
        #command ='scp -i '+ path_to_pem + " " + "-r" + files_to_share + " " +"ubuntu@" + DNSname + ":/home/ubuntu"
        subprocess.run( ['scp', '-o', 'StrictHostKeyChecking=no' ,'-i',path_to_pem, '-r' ,files_to_share,"{}@".format(ssh_username)+public_ip+":/home/{}".format(ssh_username)]) 


    ################ Tag the ec2 for swarm ################
   # print('hahaahadsfkjasdlk;fjdaskl;`~~~~~',instance_ids)
   # number_int = 1
   # for instance_id in instance_ids:
   #     number_str = str(number_int)
   #     client_ec2.create_tags(
   #         Resources=[instance_id],
   #         Tags=[
   #             {
   #                 'Key': 'Node-00'+number_str,
   #                 'Value': 'Node-00'+number_str
   #             }
   #         ]
   #     )
   #     number_int+=1

