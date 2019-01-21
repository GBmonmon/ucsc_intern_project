#!/bin/bash

AWS_DEFAULT_REGION="us-west-1"
export AWS_DEFAULT_REGION


#rm -rf .vagrant
vagrant up
vagrant status



unset AWS_DEFAULT_REGION
