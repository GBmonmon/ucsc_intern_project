#!/bin/bash

echo "--------------git command--------------"
echo "<git reset [--hard] [target reference]>"
echo "<git revert [commit sha]>"

read -p "Enter your command: " command

if [ "$command" == "git reset [--hard] [target reference]" ]; then
  echo "git reset [--hard] [target reference]"
  echo "Switch current branch to the target reference, and leave a difference as an uncommited changes. When --hard is used, all changes are discarded."
  echo "----------your commits----------" 
  git log --oneline
  read -p "Enter the target reference: " tr
  git reset --hard "$tr"
fi


if [ "$command" == "git revert [commit sha]" ]; then
  echo "git revert [commit sha]"
  echo "Create a new commit, reverting changes from the specified commit. It generates an inversion of changes."
  echo "----------your commits----------" 
  git log --oneline
  read -p "Enter the commit sha: " cs
  git revert "$cs"
fi
