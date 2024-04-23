#!/bin/bash

echo updating
sudo apt update -y
echo finished updating

echo upgrading
sudo DEBIAN_FRONTEND=noninteractive apt upgrade -y
echo finished upgrading

echo installing nginx
sudo DEBIAN_FRONTEND=noninteractive apt install nginx -y
echo finished installing nginx

# configure reverse proxy
# changing a config file

echo restarting nginx
sudo systemctl restart nginx
echo finished restarting nginx

echo enabling nginx
sudo systemctl enable nginx
echo finished enabling nginx

echo installing nodejs v20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo DEBIAN_FRONTEND=noninteractive -E bash - &&\
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs
echo finished installing nodejs v20

echo checking node version
node -v
echo finished checking node version

echo getting app folder
git clone https://github.com/LewisTowart/tech258_sparta_test_app.git
echo got app folder

echo going to app folder
cd ~/tech258_sparta_test_app/app
echo in app folder

echo installing app
npm install
echo finished installing app

echo installing pm2
sudo npm install -g pm2
echo pm2 installed

echo stop all processes
sudo pm2 stop all #app instead of all
echo

echo running app
pm2 start node app.js # app after
echo done