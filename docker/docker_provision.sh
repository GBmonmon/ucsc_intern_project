# updata yum
sudo yum -y update

# install docker
sudo yum install -y docker

# start the docker
sudo service docker start

# Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
sudo usermod -a -G docker ec2-user

# Verify
docker info

# pull the tomcat image
docker pull gbmonmon/tomcat8.0:latest

# Create a repo in this ec2 for bindmount
sudo mkdir /home/ec2-user/myapp

# create my first html
sudo touch /home/ec2-user/myapp/index.html
sudo chmod 777 /home/ec2-user/myapp/index.html
echo "Cat is cute\!" >> /home/ec2-user/myapp/index.html

# run a container 
docker container run -p 80:8080 -d --name tomcat8_server -v /home/ec2-user/myapp:/usr/local/tomcat/webapps/myapp gbmonmon/tomcat8.0:latest




