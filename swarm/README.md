# Vagrant + AWS + Docker Swarm
This example creates 3 ec2 instance running voting app, which is composed of 5 containers randomly spreading the 3 vagrant-generated instances.

### Content
1. **load.py** it will run vagrantup.py swarminit.py services.py
2. **Vagrantfile** it contains needed values for aws to work. We will get them from aws-multiple.json.
3. **aws-multiple.json** it has the values we need to create ec2
4. **vagrantup.py** it will run vagrant up to create ec2 instances and upload all the files and folders in to our ec2 instance via **scp**
5. **swarminit.py** it will join three ec2 for docker orchestrator to assign containers. it will also create a overlay network for docker swarm.
6. **services.py** it will deploy the yamlfile, **vote-stacks.yml** on ec2. Remember that we have this file because we already use scp to upload all the files.
7. **provision/installdocker.sh** Bash script run by Vagrantfile to install docker.
8. **subprocess/DNSname.sh** For vagrantup.up to know where to send the files needed
9. **subprocess/vagrantup.sh** Bash script that will run the vagrant up with **export AWS_DEFAULT_REGION="us-west-1"**. It is needed by vagrantup.py

### Hard-coded values in aws-multiple.json
1. ssh key
2. aws key pair name
3. absolute path to pem file
4. ami id
5. security group id
6. subnet id
7. vpc id
8. ssh user name




### Docker swarm deloyed on aws ec2 instances <3 nodoes>

create two security groups with the following name and port:

important: name your security group to be swarm-manager!!!!!!

### Inbound to Swarm Managers (superset of worker ports)
|Type|Protocol|Ports|Source|
|----|--------|-----|------|
|Custom TCP Rule|TCP|2377|swarm + remote mgmt|
|Custom TCP Rule|TCP|7946|swarm|
|Custom UDP Rule|UDP|7946|swarm|
|Custom UDP Rule|UDP|4789|swarm|
|Custom Protocol|50|all|swarm|


### Inbound to Swarm Workers
|Type|Protocol|Ports|Source|
|----|--------|-----|------|
|Custom TCP Rule|TCP|7946|swarm|
|Custom UDP Rule|UDP|7946|swarm|
|Custom UDP Rule|UDP|4789|swarm|
|Custom Protocol|50|all|swarm|


### For voting app, add the following ports
|Type|Protocol|Ports|Source|
|----|--------|-----|------|
|Custom TCP Rule|TCP|5000|vote-site|
|Custom TCP Rule|TCP|5001|result-site|


1. python vagrantup.py <----- This will create 3 instances on AWS.<br/>
<pre><code>**Related program**
vagrantup.py
|    swarm/subprocess/DNSname.sh
|    swarm/subprocess/vagrantup.sh
</pre></code>
2. python swarminit.py <----- This will create a 3-node swarm service.<br/>
<pre><code>**Related program**
swarminit.py
|    None
|    None
</pre></code>
3. python services.py  <----- This will run a example voting app provided by docker hub.<br/>
<pre><code>**Related program**
services.py
|    swarm/vote-stacks.yml
|    None
</pre></code>




notice: subprocess repo is some bash programs needed for the python 

