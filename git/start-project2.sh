#!/bin/bash

url=$1

if [ $# != 1 ]; then 
  echo "Usage > ./startProject2 url"
else
  git init 
  git clone $url
echo "
/logs/*
!logs/.gitkeep
/tmp
*.swp
*.swo
" >.gitignore

  
fi 
