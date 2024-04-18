# Deploy a Nginx webpage on a EC2

### Step 1. Log In

Make sure you are logged into your account and that the correct region has been selected in our case that's Ireland. 

![ireland.png](Markdown_Images%2Fireland.png)

### Step 2. Navigate to EC2

Using the search bar look up EC2 and make sure you are on the landing page.

![ec2_page.png](Markdown_Images%2Fec2_page.png)

### Step 3. Launch Instance

Now we are going to start the process of launching our instance. Navigate to the launch istance button as seen below.

![launch_instance.png](Markdown_Images%2Flaunch_instance.png)

### Step 4. Name and Image choice

Here we are going to name our instance something appropriate such as tech258_lewis_task and then select the image we are looking to use in this example case that will be Ubuntu. It's important to not you can search for an image or select your own custom one.

![name_image.png](Markdown_Images%2Fname_image.png)

### Step 5. Instance type and Key pair

Next we are going to select our instance type. This refers to the specs we are looking to have on our virtual machine. In this example and training we will go with the free one which is t2.micro. t2 references the most basic machines AWS have available and the choice of size depends on the tasks we have set out to do.

After you can see Key pair. This is referencing access to the instance using a public and private SSH key pair. These have already been setup for us so in this case I select Tech258. There is an option to create a new key pair which can be used when one does not readily exist.

![instance_key.png](Markdown_Images%2Finstance_key.png)

### Step 6. Network Settings

This is the part where you can set your network settings and edit your security groups for the firewall. This shows what can access the instance such as SSH or HTTP requests. These can be created which I will also show below but for us we can use our previously created group tech258_lewis_basic_sg.

![network_previous.png](Markdown_Images%2Fnetwork_previous.png)

In the image below you can see what it looks like to create a new security group. Similar to before we want to follow an intelligent naming system I have gone with tech258_lewis_sg_task. You can also see I have added SSH and HTTP requests to be allowed to interact with the instance. The IP stating 0.0.0.0/0 essentially means that no specific IP is needed to access the instance. It can be accessed by anyone anywhere. You can change this to select IP addresses if you only one select PCs to be able to interact with the instance.

![security_new.png](Markdown_Images%2Fsecurity_new.png)

### Step 7. Final checks

On the right hand side you can see the final summary before you launch your instance. There are also options available to configure available storage and some advanced settings. We will now launch our instance.

![advanced_launch.png](Markdown_Images%2Fadvanced_launch.png)

### Step 8. Successful Launch and Connect

In the image below you can see we have launched successfully and can now click into our new id.

![success.png](Markdown_Images%2Fsuccess.png)

We can now see the information assigned with our instance, they can sometimes take a little bit of time to start running. You are going to want to again click the id as seen in the picture below.

![instance_info.png](Markdown_Images%2Finstance_info.png)

Once in we can see various details such as the assigned IPs and further down the security group which can be edited again after the launch. We now want to click the connect button in the top right to start using our instance.

![connect.png](Markdown_Images%2Fconnect.png)

### Step 9. Accessing and Using our Instance

AWS is going to kindly now show us all the commands that we will enter into git bash to access our instance.

![aws_connect.png](Markdown_Images%2Faws_connect.png)

We are now going to open git bash and work our way through the commands explaining each one as we go.

First we need to locate and navigate to our .ssh folder where our private key is located to be granted access to our instance. We are using the cd command to take us back to a base directory ~ where .ssh is located. Then we are using cd .ssh to go into the folder.

![locate_ssh.png](Markdown_Images%2Flocate_ssh.png)

Next we run the chmod 400 "tech258.pem" as a security check to make sure our private key isn't publicly viewable. Then after we run the ssh -i "tech258.pem" ubuntu@ec2-3-249-76-242.eu-west-1.compute.amazonaws.com command which is using our private key to access our instance which we will now be able to use.

![access_instance.png](Markdown_Images%2Faccess_instance.png)

### Step 10. Updating and Upgrading packages

Next we are going to run the sudo apt update -y command to get any update to our current package and download them. sudo stands for super user do which gives a high level of permissions. The -y stands for yes as this command without it would ask if we are sure, automating this and skipping the step.

![sudo_update.png](Markdown_Images%2Fsudo_update.png)

Now we are going to run the command sudo apt upgrade -y which now installs the updated packages we have just downloaded.

![sudo_upgrade.png](Markdown_Images%2Fsudo_upgrade.png)

### Step 11. Installing Nginx and Deploying our Webpage

We are now able to use the command *sudo apt install nginx -y* to install nginx which allows us to deploy a webpage.

![sudo_nginx.png](Markdown_Images%2Fsudo_nginx.png)

The command *systemctl status nginx* lets us check the status of our newly deployed webpage. You can press Q to return to the usual input section of the terminal.

![nginx_status.png](Markdown_Images%2Fnginx_status.png)

If we now go back to our instance details page where the IP addresses were located and copy the one that if public.

![pub_ip.png](Markdown_Images%2Fpub_ip.png)

Finally, paste that into a new webpage search bar, and you will see our newly deployed webpage.

![webpage.png](Markdown_Images%2Fwebpage.png)

### Step 12. Terminating our Instance

The last step we need to do in our case and many is to terminate our instance before close of business. To do this we need to go back to the instances section on AWS and search for our instance name tech258_lewis_task. Make sure to click the box next to it before moving on.

![instance_tick.png](Markdown_Images%2Finstance_tick.png)

Now navigate to the top right of the page and click the drop-down instance state. Here you will see terminate instance which you will now click on. You will finally be asked to confirm click terminate again to confirm.

![terminate.png](Markdown_Images%2Fterminate.png)


