# Vagrant + AWS + Kubernetes
This project create three ec2 instances running voter app with kuberentes. 

### Content
1. **load.py** it will run vagrantup.py, clusterinit.py, kubectlcreate.py in order.
2. **Vagrantfile** contains values that we get from aws-multiple.json which are needed for AWS.
3. **aws-multiple.json** values needed
4. **vagrantup.py** It will run ./subprocess/vagrantup.sh and ./subprocess/DNSname.sh to create three ec2 instances
5. **clusterinit.py** this will create a kubernetes cluster inside those three ec2. Network we will be using is Flannel.
6. **kubectlcreate.py** will deploy create namespace called vote and deploy app based on voteapp-deploy.yml
7. **subprocess/check_kube-system.sh**  is needed from clusterinit.py since the network has to be up and running before we join the nodes
8. **subprocess/DNSname.sh and subprocess/vagrantup.sh** is needed for vagrantup.py to work

### Hard-coded values in aws-multiple.json
1. ssh key
2. aws key pair name
3. absolute path to pem file
4. ami id
5. security group id
6. subnet id
7. vpc id
8. ssh user name


### Inbound to Kubernetes Master Node (security group)
|Type|Protocol|Ports|Purpose|
|----|--------|-----|------|
|Custom TCP Rule|TCP|443|Kubernetes API server|
|Custom TCP Rule|TCP|2379|etcd server client API|
|Custom TCP Rule|TCP|2380|etcd server client API|
|Custom TCP Rule|TCP|80|http|
|Custom TCP Rule|TCP|22|ssh|
|Custom TCP Rule|TCP|31000-32767|External Application Consumers|
|Custom UDP Rule|UDP|8285|flannel overlay network|
|Custom UDP Rule|UDP|8472|flannel overlay network|


### Inbound to Kubernetes Worker Node (security group)
|Type|Protocol|Ports|Purpose|
|----|--------|-----|------|
|Custom TCP Rule|TCP|10250|Kubelet healthcheck port|
|Custom TCP Rule|TCP|31000-32767|External Application Consumers|
|Custom UDP Rule|UDP|8285|flannel overlay network|
|Custom UDP Rule|UDP|8472|flannel overlay network|
|Custom TCP Rule|TCP|179|Calico BGP network|
|Custom TCP Rule|TCP|2379|etcd server client API (only required if using flannel, Calica)|
|Custom TCP Rule|TCP|2380|etcd server client API (only required if using flannel, Calica)|
|Custom TCP Rule|TCP|80|http|
|Custom TCP Rule|TCP|22|ssh|

### small reminder
When the kubernetes docker cluster is creaeted, it required network addon, which will run as container. For our kubernetes cluster, we will be using Flannel.
