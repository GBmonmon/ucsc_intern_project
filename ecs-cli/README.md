# AWS ECS cluster + Docker swarm
In the previous project, we only have the ability to make sure all the container could be recreated if they are down without affect the our webapp. We use docker swarm and kubernetes. They both provide the container orchestrator to make sure those containers is running. But we did not have a machanism to protect the ec2 itself.

ECS provides a service that will recover those ec2 instances inside the cluster if they are down. With that, By applying our docker swarm or kubernetes for that matter, We could confidently guarantee that out webapp is always up and running even sometime the containers are down or ec2 machines are down.

### Content
1. **load.py** will run runCluster.py, swarminit.py, services.py in order and continue asking you to run nodecheck.py.
2. **runCluster.py** first, it runs subprocess/runCluster.sh to create a ec2 Cluster and it will create the necessary ports for docker swarm and voteapp itself. Please see the follow table. 
3. **swarminit.py** it starts the swarm mode and joins 3 nodes under it.
4. **services.py** it deploys voteapp based on vote-stacks.yml. 
5. **nodecheck.py** this will rejoin a ECS recreated ec2 back to docker swarm. Under laod.py, it will keep asking you to run nodecheck.py. The thing you can do if you wanna test it out is that you can manually terminate the one ec2 under ECS cluster and run node check.
6. **docker-compose.yml, provision.py, downTasks.sh, runTasks.sh, mysql_image/, tomcat_image/** is not needed. They are a simply app that you can also run. But voting app is much cooler.


### Hard-coded values in subprocess/runCluster.sh
1. --region
2. --default-launch-type
3. --cluster
4. --access-key
5. --secret-key
6. --profile-name
7. --keypair
8. --capability-iam
9. --size
10. --instance-type
**Reminder: runCluster.py will create a security group with the following ports open for you.**


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

# Voter app
A web page that takes in vote
