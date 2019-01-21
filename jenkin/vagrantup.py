import ast
import subprocess
from subprocess import call
import os
import sys
import json

with open('aws-multiple.json', 'r') as fh:
    json_data = json.load(fh)

path_to_pem = json_data['manager']['ssh_private_key_path']
ssh_username = json_data['manager']['ssh_username']



files_to_share = os.getcwd()
print('File to share: ',files_to_share)

subprocess.run("./subprocess/vagrantup.sh")
    
result = subprocess.run("./subprocess/DNSname.sh", stdout=subprocess.PIPE )
outs = result.stdout.decode()
outs = ast.literal_eval(outs)
DNSnames = [ i.strip() for i in outs] 
print('DNSnames:' ,DNSnames)


print("""
##########################################
# scp all files in current folder to /home/ubuntu
##########################################
""")
for DNSname in DNSnames:
    print('running command: ')
    #command ='scp -i '+ path_to_pem + " " + "-r" + files_to_share + " " +"ubuntu@" + DNSname + ":/home/ubuntu"
    subprocess.run( ['scp', '-o', 'StrictHostKeyChecking=no' ,'-i',path_to_pem, '-r' ,files_to_share,"{}@".format(ssh_username)+DNSname+":/home/{}".format(ssh_username)]) 

