cd backend_VM
vagrant up
vagrant provision --provision-with deployNamekocontainer
sleep 5
cd ..
cd frontend_VM
vagrant up
vagrant provision --provision-with deployNamekocontainer
