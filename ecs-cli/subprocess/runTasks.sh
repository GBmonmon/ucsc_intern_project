#!/bin/bash

################################################
# required env <put those env to .bash_profile>
################################################
# docker_passwd
# docker_user
# docker_repo






docker login -p $docker_passwd -u $docker_user


################################################
# Build a custom tomcat image  
################################################
docker image rm --force customtomcat
docker image build -t customtomcat ./tomcat_image
docker image tag customtomcat $docker_repo/customtomcat
docker push $docker_repo/customtomcat



################################################
# Build a custom mysql image  
################################################
docker image rm --force custommysql
docker image build -t custommysql ./mysql_image
docker image tag custommysql $docker_repo/custommysql
docker push $docker_repo/custommysql


# Create a task definition and run the task
ecs-cli compose -f docker-compose.yml up

# show the containers that is running
ecs-cli ps

