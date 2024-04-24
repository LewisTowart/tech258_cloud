# Deploying An App

We are creating a script to automate the deployment of an app. To note all the echo commands are what will be printed to the terminal as the script progresses.

## Making a Script

### Step 1.

First we are making a file that can house the script we are going to be making. This file need to end in .sh which makes it a shell script that can be ran. The nano creates the file and allows us to edit the contents. This is where we need to type/paste our full script.

```
nano name.sh
```

### Step 2.

Now all you need to do is run the script by typing out the name within it's directory.

```
name.sh
```

## Full Process

### Step 1.

We need to start by updating the current list of packages checking for updates.

```
echo updating...
sudo apt update -y
echo done!
```

### Step 2.

Now we need to upgrade the list of pacakges installing the newly downloaded updates.

Its important to follow the below code when automating so that the script can skip the user input step.

```
echo upgrade packages...
sudo DEBIAN_FRONTEND=noninteractive apt upgrade -y
echo done!
```

### Step 3.

Next we are going to install nginx with similar code to step two avoiding having to take a user input for the purple kernal update box.

```
echo installing nginx
sudo DEBIAN_FRONTEND=noninteractive apt install nginx -y
echo finished installing nginx
```

### Step 4.

Here we are adding a reverse proxy this makes it so that if you go to the puclic IP it takes you to port 3000 straight away

```
# configure reverse proxy
sudo sed -i '51s/.*/\t        proxy_pass http:\/\/localhost:3000;/' /etc/nginx/sites-enabled/default
# changing a config file, replacing line 51 the local host address
```

Now we need to restart nginx so that the new config can be updated

```
echo restarting nginx
sudo systemctl restart nginx
echo finished restarting nginx
```

### Step 5.

Here we are enabling nginx so that it will be ready to go each time in the instance

```
echo enabling nginx
sudo systemctl enable nginx
echo finished enabling nginx
```

### Step 6.

We are now installing the correct node.js version

```
echo installing nodejs v20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo DEBIAN_FRONTEND=noninteractive -E bash - &&\
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs
echo finished installing nodejs v20
```

### Step 7.

Now we need to set an evironment variable with the private IP of our database in the IP area. This is connecting our app to our data base.

```
# set db_host env var
export DB_HOST=mongodb://172.31.43.234:27017/posts 
# Private IP goes in there for the database
# So the app can communicate with the data base specifically using my private IP for my Database, end point to connect to the database
```

The command below can be used to make sure we got the correct node version and it has installed

```
echo checking node version
node -v
echo finished checking node version
```

### Step 8.

From Git Hub we need to clone our repository that our app code is in as seen by the command below.

```
echo getting app folder
git clone https://github.com/LewisTowart/tech258-sparta-test-app.git
echo got app folder
```

### Step 9.

Here we will make sure that we are in the correct directory for the app code that we have just cloned in.

```
echo going to app folder
cd ~/tech258-sparta-test-app/app
echo in app folder
```

### Step 10.

Next we will install npm

```
echo installing app
npm install
echo finished installing app
```

### Step 11.

Then we need to install the process manager.

```
echo installing pm2
sudo npm install -g pm2
echo pm2 installed
```

### Step 12.

To make sure the script runs everytime with no issue we will stop processes here

```
echo stop all processes
sudo pm2 stop all #app instead of all
echo
```

### Step 13.

Finally we are going to run our app

```
echo running app
pm2 start node app.js # app after
echo done
```