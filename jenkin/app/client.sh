#!/bin/bash

#services=$(curl 10.0.1.16/grab/)
#echo $services


bol=true

while $bol; do

  echo "
files available
1. a.txt
2. b.txt
3. c.txt
4. d.txt
  
tpye exit() to end the program
"
  
  read -p "What kind of info do you want from the backend machine <Ubuntu> ? " info 

  
  if [ $info == "exit()" ]; then
    bol=false
    break
  else
    echo "Enter: exit()"
  fi

  
  if [ $info == "a.txt" ] || [ $info == "b.txt" ] || [ $info == "c.txt" ] || [ $info == "d.txt" ]; then
    data=$(curl "10.0.1.16/files/$info")  
    wget "10.0.1.16/files/$info"
    bol=false
  else
    continue
   
  fi
  
done

