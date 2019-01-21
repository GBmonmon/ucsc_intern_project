#!/bin/bash

# Create a cluster configuration
ecs-cli configure --cluster ecs-cluster-1 --region us-west-1 --default-launch-type EC2

# Create a profile using your access key and secret key
ecs-cli configure profile --access-key $Zadmin_AWS_ACCESS_KEY_ID --secret-key $Zadmin_AWS_SECRET_ACCESS_KEY --profile-name ecs-cluster-1


# Create cluster
ecs-cli up --force --keypair admin-key-us-west-1 --capability-iam ami-0bdb828fd58c52235 --size 3 --instance-type t2.micro

ecs-cli scale --capability-iam --size 3 --cluster ecs-cluster-1 --region us-west-1
