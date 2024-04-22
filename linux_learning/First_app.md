# Deploying my first App

We are creating a script to automate the deployment of an app.

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