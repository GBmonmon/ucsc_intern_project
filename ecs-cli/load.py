import subprocess
import os
filenames = ['runCluster.py', 'swarminit.py', 'services.py']

for fh in filenames:
    input('Press enter to run: %s'%(fh,))
    os.system('python {}'.format(fh)) 

nodecheck = 'nodecheck.py'
bol = True
while bol:
    print('\nType exit() to leave.')
    inp = input('Press enter to run: %s\n'%(nodecheck,)) 
    if inp != "exit()" and inp == "":
        os.system('python {}'.format(nodecheck))
    if inp == "exit()":
        bol = False
        break  
    if inp != "exit()": continue
    
