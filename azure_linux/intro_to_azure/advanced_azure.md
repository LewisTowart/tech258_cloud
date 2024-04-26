# Advanced Azure

### MongoDB open port azure

on default sg rule on azure is to allow any internal traffic on your internal network. All devices internal on the inside of your virtual network can talk to each other ragrless of their subnet.

Like the Virtual network is an apartment the subnets are the rooms. Azure can walk between the rooms and talk to each other. On AWS you can't only in the same room.

AWS you need to open the port for internal traffic.

### Public instead of private

we have only set rules for incoming traffic so far

you would have to open the 27017 port on the inbound of the database to use the public IP

# Levels of automation

we are putting our vms in our virtual network

from an image database will always start mongodb is enabled

for the app it wont because pm2 is not a system process cant be enabled

will need some user data to cd into the app folder and start pm2

commands will only run as fast they can so speed to deploy is faster as you are skipping steps you need to take but they still need to run

speed of the app increase at image because those commands don't need to be ran

user data runs as root so will use sudo whether you put it or not
starting directory will be the root folder /
only runs on the start up of the vm

try to get one script that works in user data and ssh in

how to delete your vm properly section
