#!/bin/bash

aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro" "Name=instance-state-name,Values=running" "Name=instance.group-name,Values=swarm-manager" --query "Reservations[].Instances[].PublicDnsName"
