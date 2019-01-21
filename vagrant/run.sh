#!/bin/bash

# set env
AWS_DEFAULT_REGION="us-west-1"
export AWS_DEFAULT_REGION

# Create a ec2 instance
vagrant up

# Status
vagrant status
echo "Instance is running."

echo "-----------instance info------------" 
id=$(aws ec2 describe-instances --filters "Name=instance-state-code,Values=16" "Name=tag:Name,Values=tomcat_in_ec2" --query "Reservations[*].Instances[*].InstanceId" --output text)
echo "InstanceId > $id"
ip4=$(aws ec2 describe-instances --instance-ids "${id}" --query 'Reservations[*].Instances[*].PublicIpAddress' --output text)
echo "Ip4 > ${ip4}"
url=$(echo "http://${ip4}:8080")
echo "Open the page by this url: ${url}"


#remove env for security purposes
unset AWS_DEFAULT_REGION
