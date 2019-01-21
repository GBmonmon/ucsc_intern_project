#!/bin/bash
echo "--------------git command--------------"
echo "<git status>
<git diff> 
<git checkout -- [file]> 
<git add [file]>
<git reset [file]>
<git commit -m>
<git rm [file]>
<git stash>
"
read -p "Enter your git command: " command

#git status
if [ "$command" == "git status" ]; then
  echo "Usage > git status"
  echo "See the status of your work. New, staged, modified files. Current branch."
  git status
fi


## git diff and git diff --staged
if [ "$command" == "git diff" ]; then
  echo "Usage > 1. git diff [file] 
        2. git diff --staged [file]"
  bol=true
  while [ "$bol" == true ]; do
    read -p "Choose a usage 1 or 2: " diffcommand
    if [ "$diffcommand" == 1 ]; then
      echo "you are using: git diff [file]"
      echo "Show changes between working directory and staging area."
      read -p "Enter the file you want to see the changes: " filename
      git diff ${filename} 2>> /dev/null      
      bol=false
    elif [ "$diffcommand" == 2 ]; then
      echo 'you are using: git diff --staged [file]'
      echo 'Show changes between staging area and index (repository commited status).'
      read -p " Enter the file you want to see the changes: " filename
      git diff --staged ${filename} 2>> /dev/null
      bol=false    
    fi
  done
fi
  

## git checkout -- [file]
if [ "${command}" == "git checkout -- [file]" ]; then
  echo "Usage > git checkout -- [file]"
  echo "Discard changes in working directory. This operation is unrecoverable. It will go back to your last commit for this file"
  read -p "Enter the file your want it to discard the changes you made in the working directory going back to the last commit of this file: " filename
  git checkout -- "${filename}"
fi


## git add [file]
if [ "${command}" == "git add [file]" ]; then 
  echo "Usage > 1. git add [file]"
  echo "        2. git add ."
  echo "        3. git add -A"
  bol=true
  while [ ${bol} == true ]; do
    read -p "Choose a usage 1 or 2 or 3: " addcommand
    if [ "${addcommand}" == 1 ]; then
      echo "git add [file]"
      echo "Add a file to the staging area"
      read -p "Enter the file you want to add to the staging area: " filename
      git add "${filename}"
      bol=false
    elif [ "${addcommand}" == 2 ]; then
      echo "git add ."
      echo "Add those modified and new files to the staging area (you can use git status to check them.)"
      git add .
      bol=false
    elif [ "${addcommand}" == 3 ]; then
      echo "git add -A"
      echo "Add all the file to staging area."
      git add -A
      bol=false
    fi
  done 
fi
  

## git reset [file]
if [ "${command}" == "git reset [file]"  ]; then
  echo "Usage git reset [file]"
  echo "Get file back from staging area to working directory"
  read -p "Enter the file you want it out of the staging area: " resetfile
  git reset "${resetfile}"
fi


## git commit -m "message of this commit"
if [ "${command}" == "git commit -m" ]; then
  echo "Usage git commit -m \"message of this commit\""
  echo "Create new commit from changes add to the staging area. Commit must have a message!"
  read -p "message of this commit: " commitMessage
  git commit -m "\"${commitMessage}\""
fi


# git rm [file]
if [ "${command}" == "git rm [file]" ]; then
  echo "Usage git rm [file]"
  echo "Remove file from working directory and add deletion to staging area"
  read -p "Enter file you want to remove from the working directory and add deletion to staging area: " filename
  git rm "${filename}"
fi


# git stash
if [ "${command}" == "git stash" ]; then
  echo "Usage > 1. git stash save
        2. git stash list
        3. git stash apply [stashID]
        4. git stash pop
        5. git stash drop"
  bol=true
  while [ "${bol}" == true ]; do
    read -p "Choose 1, 2, 3, 4, 5: " stashcommand
    if [ "${stashcommand}" == 1 ]; then
      echo "git stash save"
      echo "Put your current changes into stash"
      read -p "Enter file you want to stash: " filename
      git stash save "${filename}"
      bol=false
    elif [ "${stashcommand}" == 2 ]; then
      echo "git stash list"
      echo "List your stash"
      git stash list
      bol=false
    elif [ "${stashcommand}"  == 3 ]; then
      echo "git stash apply [stashID] "
      echo "In order to use the stash, you need to provide stashID such as: stash@{0}" 
      read -p "Enter the stashID: " stashID
      git stash apply "${stashID}"
      bol=false
    elif [ "${stashcommand}" == 4 ]; then
      echo "git stash pop"
      echo "Apply stored stash content into working directory, and clear stash with zero ID"
      git stash pop
      bol=false
    elif [ "${stashcommand}" == 5 ]; then
      echo "git stash drop"
      echo "Clear stash without applying it into working directory."
      read -p "Type in the stashID you want to drop, use git stash list to see the id: " stashid
      git stash drop "${stashid}"
      bol=false
    fi
  done


fi 
