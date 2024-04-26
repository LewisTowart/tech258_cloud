To do
When creating your database VM, find the section for user data - paste in your full database script so that you only need to SSH in to check the script in user data worked successfully to install + configure mongo DB
When creating your app VM, find the section for user data - paste in your full app script so that the posts page works.

About user data:
runs as root user (i.e. every command will be run as sudo whether you've put sudo in the command or not)
starting file location is /
only runs once immediately after VM is created

Hints:
Only use user data if you are 100% confident in your Bash script
You may need to modify your Bash scripts based on the above points.  For example:
If you use relative paths when setting up your app folder, consider the different starting file location when user data runs
Don't worry about any command in your script that already uses sudo - it will still run fine in user data
It is possible to troubleshoot user data, but it is more challenging - you will need to look at a particular log file


Once you have the database VM running and configured correctly, create an image of it.  Name it similar to `tech258-yourname-ubuntu2204-db-ready-to-run`
Use this new pre-provisioned database image to create a new database VM
Once you have the app VM running the app, create an image of it.  Name it similar to `tech258-yourname-ubuntu2204-app-ready-to-run`
Use this new pre-provisioned app image to create a new app VM
However, first make sure you database VM is already running
Then when creating the app VM with your newly created app image, paste in the user data from your app provision script for just starting the app - you want the posts page to work.  Your little bit of user data should:
set DB_HOST
cd into the app folder
run npm install
run the app with pm2
As soon as your posts page is working, paste a link to it in the main chat.
Document, include:
What is an Azure Image - what does it include, what is the equivalent called on AWS
What is not included in the image and why
What is the side-effect of creating an image of a VM on Azure? (After creating the image, can you log back into the VM used to create the image?)
The little bit of user data needed to get the app running with the posts page (and what can be commented out if you don't need the posts page to work)
Post the link to your documentation in the main chat at COB.
Clean up all your VMs + associated parts.  Leave your `ready-to-run` app and database images - we will need them next week.