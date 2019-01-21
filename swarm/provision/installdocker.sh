######################################
## Set up the docker repository
######################################
#sudo apt remove docker docker-engine docker.io 2> /dev/null
#sudo apt update -y 
#sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
#sudo apt update -y
#apt-cache policy docker-ce
#
######################################
## Install Docker CE
######################################
#sudo apt update -y
#sudo apt install docker-ce -y
#
#
#
######################################
## Verify the installation
######################################
##sudo docker run hello-world
#
#
#
######################################
## Run docker without sudo
######################################
#sudo usermod -a -G docker ${USER}


#sudo yum update -y
#sudo yum install -y docker
#sudo service docker start
#sudo usermod -a -G docker ec2-user
