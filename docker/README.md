# Vagrant + AWS + Docker
In this project, we use the Vagrantfile to create a ec2 instance, a cloud machine with computing power, for our dockerized program to run on. This simple app is a Django container retrieves data in MySQL container. 

### Content
1. **Vagrantfile**: This file is used by Vagrant to spin up the AWS instance. You must change the path to your SSH private key. You must supply the correct name to the dummy box installed for AWS.
2. **app-stack.yml** This yaml file will create two containers with nessesary env and ports

### Hard-coded values in Vagrantfile
1. ssh key
2. aws key pair name
3. absolute path to pem file
4. ami id
5. security group id
6. subnet id
7. vpc id
8. ssh user name

### Little reminder
Vagrant requires that a "dummy box" be installed for use with AWS. Run this command to install the dummy box:

1. vagrant box add <box-name> https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box

2. Install the Vagrant AWS provider by running `vagrant plugin install vagrant-aws`.

3. Remember to type in your 1. aws access key, 2. aws secret access key. Or you can 


### Docker basic command
|command|purpose|
|----|--------|
|docker container ls|List all running containers|
|docker container ls -a|List all containers, including the exist one|
|docker container run --detached image|Run a container from a image in the background|
|docker image ls|List all the downloaded image|
|docker image pull folder/name:version|Pull the image down|
|docker network ls|List all the network|



