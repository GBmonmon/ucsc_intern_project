from clusterinit import SSHclient

if __name__ == '__main__':
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
    manager1_ssh = SSHclient(host_ip=managers_ip[0], port=22, username=ssh_username, key=path_to_pem)
    manager1_ssh.execute('kubectl create namespace vote')
    manager1_ssh.execute('kubectl create -f $HOME/kuber/voteapp-deploy/')
    manager1_ssh.close()
    

    vote_url1 = 'http://'+ managers_ip[0]+':31000'
    vote_url2 = 'http://'+workers_ip[0]+':31000'
    vote_url3 = 'http://'+workers_ip[1]+':31000'
    result_url1 = 'http://'+managers_ip[0]+':31001'
    result_url2 = 'http://'+workers_ip[0]+':31001'
    result_url3 = 'http://'+workers_ip[1]+':31001'
    print(""""
    #########################################################
    # URL
    #########################################################
    """)
    print('Vote site URL:\n'+vote_url1 + '\n' + vote_url2 + '\n' + vote_url3 + '\n\n' )
    print('Result site URL:\n'+result_url1 + '\n' + result_url2 + '\n' + result_url3 )
