### User Data

User data allows you to put a script within this field and it will be ran straight away on the start up of your instance.

In my case I was able to run my database script and my app deployment script within the user data field and have the two connect to each other being able to access my database.

Some key elements to watch out for are:

* Make sure you give your database enough time to start up before starting your app
* You must after attempting to run your script for the first time in user data ssh into your instance to make sure it is running
* Don't forget to check every option before launching the instance something as small as choosing the wrong Ubuntu version has stopped me before
* Make sure to set the correct private IP so that your app can connect with the database
* You must have a shebang e.g #!/bin/bash at the top of your script to tell the user data what shell to use or it won't run
* Make sure your script is 100% working as it is much harder to troubleshoot it after having it run through user data

Something I want to mention seperately is that all commands will be ran by the root user which means the sudo command isn't needed as it is automatically being used for each command. Having the sudo command in your script won't do anyharm but this is worth noting. The directory that the user data will start from is also / which stands for root. You can take this into account within your script for example I added the line cd ~/ which moves you into the home directory where you can now CD into your app folder.

The user data option is available in the advanced tab when creating your virtual machine

![alt text](Markdown_Images/advanced_section.PNG)

If you scroll down from here and tick the user data box, then paste your script within there it will be ready to run on the boot up if your virtual machine.

![alt text](Markdown_Images/user_data.PNG)

### Creating an image

When you have you instance running setup in the way you want for example my database having mongodb installed and enabled.

You can then go to the overview page for you instace and select capture.

You are going to want to select the correct resource group then tick the box that says "No capture only a managed image" I would also select automatically delete vm when finished. You can do this yourself manually later. You want to name it correctly then click create and give it some time to finish setting up. Don't forget to add the owner and value tags with you name.

![alt text](Markdown_Images/Capture.PNG)

This will take what is essentially a snapshot of everything that you have installed on the instance through the use of the script. For example my database image will boot up with mongo db already installed and enabled (running) ready to go.

When creating your virtual machine you need to select your newly created image.

For certificate at the bottom you can select other as Ubuntu isn't an option.

It's very important you intialise you database vm first giving it a good 4-5mins to load up fully. If you're loading from the newly created database image this will be significantly faster around a minute. After this you can intialise your app image. You can ssh into you database and run the sudo systemctl status mongod to see if it is running.

For the app image because pm2 isn't a system process you can't enable it. This means you will have to add the below script into the user data section to get it running from the newly created image.

```
#!/bin/bash

export DB_HOST=mongodb://10.0.3.6:27017/posts 

cd /repo/app

npm install

pm2 start node app.js 
```

### What is an Azure Image - what does it include, what is the equivalent called on AWS

In the context of Microsoft Azure, an "Azure Image" refers to a template that contains the operating system, applications, and other software configurations necessary to create a virtual machine (VM) within the Azure cloud environment. Essentially, it's a snapshot of a virtual machine's disk that can be used to provision multiple VMs with identical configurations.

Azure Images typically include:

1. **Operating System**: The base operating system such as Windows Server, various distributions of Linux (e.g., Ubuntu, CentOS).
2. **Pre-installed Software**: Additional software packages or applications that are included in the image.
3. **Custom Configurations**: Any custom configurations or settings applied to the operating system or installed applications.

In Amazon Web Services (AWS), the equivalent of Azure Images is called "Amazon Machine Images" (AMIs). Like Azure Images, AMIs are templates that contain the necessary information to launch EC2 instances, AWS's virtual servers. AMIs in AWS include similar components as Azure Images, such as the operating system, software applications, and configurations.

Both Azure Images and AWS AMIs serve as convenient ways to deploy standardized virtual machines quickly and consistently within their respective cloud environments.

### What is not included in the image and why

In both Azure Images and AWS AMIs, certain components or configurations are intentionally excluded. This is primarily done to maintain flexibility, minimize image size, and ensure security. Here are some examples of what is typically not included:

1. **User Data**: User data, such as files and personal configurations, are generally not included in the image. This allows users to customize instances based on their specific needs after deployment.

2. **Sensitive Information**: Confidential data, credentials, or sensitive configurations are not included to maintain security. It's crucial to avoid exposing sensitive information within shared or public images.

3. **Temporary Files**: Temporary files or caches are typically not included in the image to keep its size manageable and to prevent unnecessary bloat.

4. **Unique Identifiers**: Unique identifiers such as instance IDs or MAC addresses are not included since they are generated dynamically when instances are launched. Including them in the image would lead to conflicts and inconsistencies.

5. **Networking Configurations**: Network-specific configurations, such as IP addresses and routing tables, are not included. These settings are typically managed dynamically based on the instance's environment and deployment context.

6. **Updates and Patches**: While the base operating system and software versions are included, updates and patches released after the image creation are not. This ensures that instances launched from the image can be updated to the latest security patches and software versions during deployment.

Excluding these elements allows for greater flexibility and security when deploying instances from images. Users can customize instances, apply security updates, and adapt to changing environments without being constrained by predefined configurations included in the image.

### What is the side-effect of creating an image of a VM on Azure? (After creating the image, can you log back into the VM used to create the image?)

When you create an image of a virtual machine (VM) on Azure, it effectively captures the state of the VM at the time the image was created. One significant side effect of this process is that the original VM used to create the image is deallocated and no longer accessible in its previous state. 

Once the image creation process is complete, you can no longer log back into the original VM as it essentially ceases to exist in its previous form. Instead, you can use the created image to provision new VM instances with identical configurations as the original VM.

This behavior is common across cloud platforms like Azure and AWS when creating images or snapshots of virtual machines. It's important to understand this side effect and plan accordingly, ensuring that any necessary data or configurations are backed up or transferred before creating the image if you need to retain access to the original VM.

### The little bit of user data needed to get the app running with the posts page (and what can be commented out if you don't need the posts page to work)

The script below is what is needed to add into the user data section.

```
#!/bin/bash

export DB_HOST=mongodb://10.0.3.4:27017/posts 

cd /repo/app

npm install

pm2 start node app.js 
```

If you are looking to just get the app working but not the posts page you can comment out the part that sets the environment variable to remove the connection between the two instances.

```
#!/bin/bash

# export DB_HOST=mongodb://10.0.3.6:27017/posts 

cd /repo/app

npm install

pm2 start node app.js 
```

# Changing file permission/accessing in root

* Use sudo -E - Uses super user permissions but also passes along the environment variables to that command
* (Recurisvely) Change permissions using chmod - You can change the permission for a folder to allow the user profile access
* (Recursively) Take ownership of the folder - You can change owner ship of the folder to the user instead of root
* Temporarily login as root - You can temporarily login as root to give you the correct permission to access the folder