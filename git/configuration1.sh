#!/bin/bash

name=$1
email=$2
if [ $# != 2 ]; then
  echo "Usage > ./configuration.sh username useremail"
else
  git config --global user.name ${name}
  git config --global user.email ${email}
  git config --global color.ui auto
fi

