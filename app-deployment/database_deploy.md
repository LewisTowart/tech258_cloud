# Deploying a Database

We are creating a script to automate the deployment of a database. 

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

Next we are going to install mongodb. (break this down when have time)

```
sudo apt-get install gnupg curl

sudo rm -f /usr/share/keyrings/mongodb-server-7.0.gpg
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

sudo apt-get update

sudo DEBIAN_FRONTEND=noninteractive apt-get install -y mongodb-org=7.0.6 mongodb-org-database=7.0.6 mongodb-org-server=7.0.6 mongodb-mongosh=2.2.4 mongodb-org-mongos=7.0.6 mongodb-org-tools=7.0.6

echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-database hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-mongosh hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections
```

### Step 4.

Change the bind IP to anywhere
```
sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/' /etc/mongod.conf
```

### Step 5.

Restart mongodb to make sure our changes are intialised and in this case mongodb doesn't automatically start so this will be it's first boot up.

```
sudo systemctl restart mongod
```

### Step 6.

Finally enable mongodb so that it is running straight from boot

```
sudo systemctl enable mongod
```