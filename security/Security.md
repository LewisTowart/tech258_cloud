# Security

## VPC

![alt text](Markdown_Images/VPC-diagram.png)

DMZ de-militarised zone
NVA - Network Virtual Appliance

We currently have two VMs one for the database and one for the app. We are going to make the database more private and secure. The app and database are each inside their own subnet. The app is part of the public subnet and the database is part of the private subnet both within our virtual network.

subnet ip from 0 to 255

Public as set to 10.0.2.0/24
Private as set to 10.0.3.0/24

We are going to make a private subnet as 10.0.4.0/24.

Both our app and database have a couple of security elements currently. One is the network security groups and the other is the network interface card which is responsible for all communications going in and out.

We have a public address people use to access our virtual machines. Web traffic traffic coming from HTTP port 80. We can access them by ssh into them through their public IPs. Both internal and external traffic go through the network security group.

A network security group has rules, it needs to allow http port 80 and ssh port 22 traffic for the app. For the database we only need to allow ssh traffic.

We are going to make stricter rules for our database network security group. We are going to only allow mongodb traffic. The lower the rule priority the higher that priority is. Could do ssh 100 mongodb 101 and a rule to deny everything else.

We are also going to create the DMZ subnet. App currently communicates to the database then the database back to the app to create the posts information. We are going to make 10.0.3.0/24 our dmz subnet. 

Inside this dmz subnet we are going to need to create a vm for a network virtual appliance. At least initially we need ssh to test and configure, can remove it when it's all been set up. It will have a public ip associated so we can ssh.

We are creating this as a form of filter or firewall. We need to make sure all database requests can only go to the database vm. This will make sure that the only traffic is coming from the right source so our app/public subnet is going to be allowed to talk to the database/private subnet. We are forcing traffic through this NVA.

All our devices can currently talk to each other. Routing is referencing the path traffic can take. We want traffic from the app to go to the database via the nva. For this we need a route table "to private subnet route table". This means traffic from the app vm will use this table so it knows to let traffic go to the nva as the next hop. After the route the next place the traffic can go is next hop. Now if the traffic is from the right source our nva will forward the traffic on to the database/private subnet, this is forwarded traffic (been filtered).

If set up correctly nothing can access our database from the outside.

Our network security interface needs IP forwarding enabled on Azure portal. IP forwarding also needs to be enabled on the linux OS on our NVA VM. We are going to use IP table for our firewall settings in linux on our NVA.

colour for things such as safe traffic and potentially not safe. route from app to nva to db is safe so green. Unsafe to public ip is unsafe



