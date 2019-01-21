#!/bin/bash

status=$(kubectl get pods -n kube-system --field-selector=status.phase!=Running | wc -c 2> /dev/null)
sleep 7

if [ $status == 0 ]; then
  echo "proceed"
else
  echo "wait"
fi
