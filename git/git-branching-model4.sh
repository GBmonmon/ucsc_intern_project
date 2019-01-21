#!/bin/bash
echo "--------------git command--------------"
echo "<git branch [-a]>
<git branch [name]>
<git checkout [name]>
<git merge [from name]>
<git branch -d [name]>
"
read -p "Enter your git command: " command

#git branch [-a]
if [ "${command}" == "git branch [-a]" ]; then
  echo "git branch [-a]"
  echo "List all local branches in local repository. With -a: show all branches (with remote)"
  git branch -a
fi


#git branch [name]
if [ "${command}" == "git branch [name]" ]; then
  echo "git branch [name]"
  echo "Create new branch, referencing the current HEAD"
  read -p "Enter the new branch name you want to create: " newBranchName
  git branch "${newBranchName}"
fi


#git checkout 
if [ "${command}" == "git checkout [name]" ]; then
  echo "Usage > 1. git checkout [name]
        2. git checkout [-b] [name]"
  bol=true
  while [ "${bol}" == true ]; do
    read -p "Enter the Usage 1, 2: " checkoutCommand
    if [ "${checkoutCommand}" == 1 ]; then
      echo "git checkout [name]"
      read -p "Enter the existing branch name: " existingBranch
      git checkout "${existingBranch}"
      bol=false
    elif [ "${checkoutCommand}" == 2 ]; then
      echo "git checkout [-b] [name]"
      echo "With -b: git will create specified branch if it does not exist."
      read -p "Enter a new git branch name: " newBranchName
      git checkout -b "${newBranchName}"
      bol=false 
    fi
  done
fi


#git merge
if [ "${command}" == "git merge [from name]" ]; then
  echo "git merge [from name]"
  echo "Join specified [from name] branch into your current branch, the one your are on currently"
  read -p "Enter the branch you want to merge into the current branch your are on: " branchname
  git merge "${branchname}"
fi


#git branch -d [name]
if [ "${command}" == "git branch -d [name]" ]; then
  echo "Usage > 1. git branch -d [name]
        2. git branch -D [name]"
  bol=true
  while [ "${bol}" == true ]; do
    read -p "Enter the usage 1, 2: " branchcommand
    if [ "${branchcommand}" == 1 ]; then
      echo "git branch -d [name]"
      echo "Remove seleted branch, if it is a already merged into any other."
      read -p "Enter the branch name: " branchname
      git branch -d "${branchname}"
      bol=false
    elif [ "${branchcommand}" == 2 ]; then
      echo "git branch -D [name]"
      echo "With -D: forces deletion."
      read -p "Enter the branch name: " branchname
      git branch -D "${branchname}"
      bol=false
    fi
  done
fi



