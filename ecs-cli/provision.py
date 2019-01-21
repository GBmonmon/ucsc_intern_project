class SSHclient:
   
    "This class is for paramiko"   
    import paramiko 
    import subprocess
    import boto3
    import os
    
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
                'out':stdout.readline().rstrip('\n'),
                'error':stderror.readline().rstrip('\n') 
               } 
    
 



if __name__ == '__main__':

    import paramiko
    import subprocess
    import boto3
    import os
    import time
    # Check if ec2 is running or is still pending
    client_ec2 = boto3.client('ec2','us-west-1')

    rsp = client_ec2.describe_instances()
    #state = rsp['Reservations'][0]['Instances'][0]['State']['Name']    

    my_ip = list()
    for i in rsp['Reservations']:
        state = i['Instances'][0]['State']['Name']   
        if state == 'terminated': continue
        bol = True
        while bol:
            state = i['Instances'][0]['State']['Name']    
            if state == 'running':
                my_ip.append(i['Instances'][0]['PublicIpAddress'])
                bol = False
                break
            else:
                print('waiting...')
                time.sleep(10)
                continue
    print('-------------------------------')
    print(my_ip)
    # Create a repo, /mysql_data/data for storing   
    

    print('==============', my_ip[0],'==========')
    
    
    paramiko_client = SSHclient(host_ip=my_ip[0], port=22, username='ec2-user', key='~/.ssh/zxc22022444/ZAdministrator/admin-key-us-west-1.pem')    
    #docker_passwd = os.environ['docker_passwd']
    #docker_user = os.environ['docker_user']
    #paramiko_client.execute('export docker_passwd=\'%s\''%docker_passwd)
    #paramiko_client.execute('export docker_user=\'%s\''%docker_user)
    #paramiko_client.execute('docker login -p $docker_passwd -u $docker_user')
    paramiko_client.execute('mkdir -p /mysql_data/data', sudo=True)

    # create a DNS network for container
    paramiko_client.execute('docker network create my_app_net')
    
    #paramiko_client.close()

    

    subprocess.run('./subprocess/downTasks.sh',shell = True)
  
    subprocess.run('./subprocess/runTasks.sh')
    time.sleep(20)

    outerror = paramiko_client.execute('docker container ls  --format "{{.Names}}" | grep mysql')
    name_my = outerror['out']
    
    #paramiko_client.execute('docker exec {} bash chmod 777 /code/data.sql'.format(name_my))
    try:
        aaa = paramiko_client.execute('docker exec {} /bin/bash -c \"mysql -uroot -pgbmonmon </code/data.sql\"'.format(name_my))
        print(aaa)
        print(name_my)
 
        print('---------------------------------------------')
        outerror = paramiko_client.execute('docker container ls  --format "{{.Names}}" | grep tomcat')
        name_tom = outerror['out']    
        bbb = paramiko_client.execute('docker container exec {} /bin/bash -c \"python3 /code/tomcatQuery_fromMysql.py\"'.format(name_tom))
        print(bbb)
        print(name_tom)
        paramiko_client.close()
    except:
        os.system('python provision.py')
    print('Main page URL: http://%s'%(my_ip[0]))
    print('Data from mysql URL: http://%s/myapp'%(my_ip[0]))
