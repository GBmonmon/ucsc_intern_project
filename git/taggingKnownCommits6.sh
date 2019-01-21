#!/bin/bash
echo "--------------git command--------------"
echo "<git tag>"
echo "<git tag [name] [commit sha]>"
echo "<git tag -a [name] [commit sha] -m [message]>"
echo "<git tag -d [name]>"


read -p "Enter your git command: " command
if [ "$command" == "git tag" ]; then
  echo "git tag"
  echo "List all tags."
  git tag
fi


if [ "$command" == "git tag [name] [commit sha]" ]; then
  echo "Usage > 1. git tag [name]
        2. git tag [name] [commit sha]"
  bol=true
  while [ "$bol" == true ]; do 
    read -p "Enter the Usage 1, 2: " tagcommand
    if [ "${tagcommand}" == 1 ]; then
      echo "git tag [name]"
      echo "Create a tag reference named name from \"current commit\"."
      read -p "Enter the tag name: " tagname
      git tag $tagname
      bol=false
    elif [ "${tagcommand}" == "2" ]; then
      echo "git tag [name] [commit sha]"
      echo "Create a tag reference named name for a \"specific commit\"." 
      read -p "Enter the tag name: " tagname
      echo "---------Your log (choose the hash e.g: 180ad62)---------"
      git log --oneline
      read -p "Enter the commit sha: " commitsha
      git tag $tagname $commitsha
      bol=false
    fi
  done
fi


if [ "$command" == "git tag -a [name] [commit sha] -m [message]" ]; then
  echo "Usage > 1. git tag -a [name] -m [message]
        2. git tag -a [name] [commit sha] -m [message]"
  bol=true
  while [ "$bol" == true ]; do
    read -p "Enter the Usage 1, 2: " tagcommand
    if [ "$tagcommand" == 1 ]; then
      echo "git tag -a [name] -m [message]"
      echo "Create a tag object name named for \"current commit\"."
      read -p "Enter the tag name: " tagname
      read -p "Enter the message for this tag: " tagmessage
      git tag -a $tagname -m $tagmessage
      bol=false
    elif [ "$tagcommand" == 2 ]; then
      echo "git tag -a [name] [commit sha] -m [message]"
      echo "Create a tag object name named for \"specified commit\"."
      read -p "Enter the tag name: " tagname
      read -p "Enter the message for this tag: " tagmessage
      echo "---------Your log (choose the hash e.g: 180ad62)---------"
      git log --oneline
      read -p "Enter the commit sha: " commitsha
      git tag -a "$tagname" "$commitsha" -m "$tagmessage"      
      bol=false
    fi

  done
fi


if [ "$command" == "git tag -d [name]" ]; then
  echo "git tag -d [name]" 
  echo "Remove a tag from a local repository."
  echo "----------the tags you have----------"
  git tag
  read -p "Enter the tag name you want to delete: " tagname
  git tag -d ${tagname}
fi 
