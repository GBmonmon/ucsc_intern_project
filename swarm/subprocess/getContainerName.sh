#!/bin/bash

bol=true
while $bol; do
status=$(docker service ls --filter "Name=webapp_db" --format "{{.Replicas}}")
if [ ${status} == '1/1' ]; then
  containerName=$(docker container ls --filter "Name=webapp_db" --format "{{.Names}}")
  bol=false
  break
fi
done

echo $containerName

