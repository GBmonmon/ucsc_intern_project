# Vagrant + AWS (Single Ec2 Instance)
These files were created to allow users to use Vagrant (http://www.vagrantup.com) with AWS.

## hard-coded values in Vagrantfile
1. ssh key
2. aws key pair name
3. absolute path to pem file
4. ami id
5. security group id
6. subnet id
7. vpc id
8. ssh user name


## Content
**README.md**: some reminders
**Vagrantfile**: This file is used by Vagrant to spin up the AWS instance. You must change the path to your SSH private key. You must supply the correct name to the dummy box for AWS.

## Instruction
Vagrant requires that a "dummy box" be installed for use with AWS. Run this command to install the dummy box:

1. vagrant box add <box-name> https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box

2. Install the Vagrant AWS provider by running `vagrant plugin install vagrant-aws`.

3. Remember to type in your 1. aws access key, 2. aws secret access key. Most of the time it is under: **~/.aws**. Due to the aws plug-in issue, aws.aws_profile will not work. So we need a bash script to export and set an environment variable **AWS_DEFAULT_REGION="us-west-1"**. 
