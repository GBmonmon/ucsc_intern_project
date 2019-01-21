#!/bin/bash

aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" "Name=instance.group-name,Values=kube-master" --query "Reservations[].Instances[].PublicDnsName"
