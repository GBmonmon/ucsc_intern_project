#!/bin/bash
echo "--------------git command--------------"
echo "git fetch [remote]"
echo "git fetch --prune [remote]"
echo "git pull [remote]"
echo "git push [--tags] [remote]"
echo "git push -u [remote] [branch]"
echo "----------your remote----------"
git remote -v
echo " "
read -p "Enter the git command: " command

if [ "$command" == "git fetch [remote]" ]; then
  echo "git fetch [remote]"
  echo "Fetch changes from the remote, but not update tracking branches."
  read -p "Choose a remote (convention:origin)." remote
  git fetch $remote
fi


if [ "$command" == "git fetch --prune [remote]" ]; then
  echo "git fetch --prune [remote]"
  echo "Remove remote refs, that were removed from the remote repository."
  read -p "Choose a remote (convention:origin): " remote
  git fetch --prune $remote
fi


if [ "$command" == "git pull [remote]" ]; then
  echo "git pull [remote]"
  echo "Fetch changes from remote and merge current branch with its upstream."
  read -p "Choose a remote (convention:origin)." remote
  git pull $remote
fi


if [ "$command" == "git push [--tags] [remote]" ]; then
  echo "git pull [remote]"
  echo "Fetch changes from remote and merge current branch with its upstream."
  echo "----------your tags----------"
  git tag
  read -p "Choose a remote (convetion:origin): " remote
  git push --tags $remote 
fi


if [ "$command" == "git push -u [remote] [branch]" ]; then
  echo "git push -u [remote] [branch]"
  echo "Push local repository to the remote. Set its copy as an upstream."
  echo "----------your branch----------"
  git branch -a
  read -p "Choose the branch corresponding to the current branch your are on locally: " bra
  read -p "Choose a remote (convention:origin): " remote
  git push -u $remote $bra
fi



