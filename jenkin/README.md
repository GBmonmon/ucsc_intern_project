# 3-nodes Jenkins github-webhook

### setting up
After we run the vagrantup.py, we create three ec2 instances for our Jenkins CI. Remember, the availability zone for those three machines have to be the same. 

1. In master node, run ssh-keygen -t rsa -C "test@gmail.com" to generate 1. private ssh key and 2. public ssh key.
2. run echo "content of your pubcic key id_rsa.pub" >> ~/.ssh/authorized_keys under the slave nodes

