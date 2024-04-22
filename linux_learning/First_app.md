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
# fix this command asks for user input
# pending kernal upgrade
sudo DEBIAN_FRONTEND=noninteractive apt upgrade -y
echo done!
```

### Step 3.

Next we are going to install nginx with similar code to step two avoiding having to take a user input for the purple kernal update box.

```