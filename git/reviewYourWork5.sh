#!/bin/bash
echo "--------------git command--------------"
echo "git log [-n count]"
echo "git log [--oneline --graph --decorate]"
echo "git log ref.."
echo "git log ..ref"
echo "git reflog"

read -p "Enter your git command: " command

if [ "$command" == "git log [-n count]" ]; then
  echo "git log [-n count]"
  echo "List commit history of current branch. -n count limits list to last n commits."
  read -p "How many commits your want to list: " numberOfCommit
  git log -n $numberOfCommit
fi


if [ "$command" == "git log [--oneline --graph --decorate]" ]; then
  echo "git log [--oneline --graph --decorate]"
  echo "An overview with references labels and history graph. One commit per line."
  git log --oneline --graph --decorate
fi


if [ "$command" == "git log ref.." ]; then
  echo "git log ref.."
  echo "List commits that are present on the current branch and not merged into ref. A ref can be a branch name or a tag name."
  echo "----------------your branchs-----------------"
  git branch 
  read -p "choose a branch: " yourBranch
  git log "$yourBranch"..
  echo "^"
  echo "|"
  echo "|"
  echo "Listed commits in your current branch have not been merged into ${yourBranch}"
fi


if [ "$command" == "git log ..ref" ]; then
  echo "git log ..ref"
  echo "List commits that are present on ref and not merged into current branch."
  echo "----------------your branchs-----------------"
  git branch 
  read -p "choose a branch: " yourBranch
  git log "$yourBranch"..
  echo "^"
  echo "|"
  echo "|"
  echo "Listed commits in your current branch have not been merged into ${yourBranch}"
fi


if [ "$command" == "git reflog" ]; then
  echo "git reflog"
  echo "List operations (like checkout, commit etc) made on local repository."
  git reflog
fi
