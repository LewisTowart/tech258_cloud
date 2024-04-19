# Linux Commands

### General Commands

```
uname
uname --help
```
* uname tell you what operating systems you are using
* If you write --help afterwards you can see various other options available to you

```
whoami
```
* This command can tell you the current username

```
ps
ps -p
```
* ps prints out the current list of running processes
* You can use ps -p then name a specfic pid such as $$ which is bash to see it's running status

```
history
history -c
```
* history can show you the list of commands that have been ran and in what order
* history -c clears this history can be useful for security based purposes

### Data Transfer Commands

```
curl (url) --output (name)
```
* curl is used for data transfer in the above example you could use the url of an image and then name that file which will be downloaded then saved in the current directory

### File Based Commands

```
file (name)
```
* file with the name of a file after it can be used to get information about that file

```
mv (name) (new name)
mv (name) (new directory)
mv (file directory/name) (new directory)
```
* The first example of the move command allows you to rename a file when it is done within the current location of the file.
* In the next example you first type the file name then the new directory you want it moved to.
* If you are not in the current file location you will need to add the file path first before the file name then the new directory you want it moved to.

```
cp
cp cat cat.jpg
```
* You can use the cp command to copy file giving them a new name.

```
rm
rm cat.jpg
rm -r folder_name
rm -rf folder_name
```
* rm is used to delete/remove files and folders.
* rm file_name deletes a file.
* rm -r deletes the root directory which could be a folder and everything in it.
* rm -rf is the same but uses the force side of the command. You need to be really careful what you use this command for as it's powerful and if something doesn't want to be deleted there's probably a reason.

```
mkdir
mkdir a_folder
```
* The mkdir command makes a directory/folder somewhere of your choosing.

```
touch
touch file.txt
```
* touch create a file specficially with nothing in it's contents

```
nano
nano file.txt
```
* nano is the in built text editor for the terminal
* You can do nano (file_name) to edit an existing file or nano (new_file_name) to create and start editing a new file.

```
cat
cat file.txt
```
* cat can be used to fetch infromation from a file
* cat file.txt would print out the information within the file

```
head -n (file_name)
tail -n (file_name)
cat -n (file_name)
grep "chicken" (file_name)
```
* head start from the top of the text file and will print out the specific nuumber in -n of lines from the top e.g -3.
* tail starts from the bottom of the text file and will print out the specific number in -n of lines from the bottom e.g -1.
* cat -n will print out all of the lines of the text file numbering them top to bottom.
* grep "word" will print out every line that the word within quotation marks appears.

```
ls
ll
```
* ls will show you all the files and folder in your current directory.
* ll will do the same with more information regarding things like permission.

### Package: Tree

```
sudo apt update -y
```
* This command gets updates for current list of installed pacakges.

```
sudo apt upgrade -y
```
* This command now installs those updated packages you downloaded.

```
sudo apt install
sudo apt install tree
```
* The sudo apt install command is used to install various packages you may want.
* tree is an example of a package you can install.

```
tree
```
* With the tree package install you can use tree to clearly show the different directories and what each one contains.

### Moving Around

```
cd
cd (folder_name)
cd ..
cd /
cd home
```
* cd is used to move around if you use cd by itself you will be taken back to the user directory.
* cd then the name of a folder will take you into that directory.
* cd .. will take you back one directory.
* cd / will take you back to the root directory.
* cd home will take you to the home directory.

### Script file/Permissions

Permissions are very important to show who can access a file.

The three groups are:
* Owner
* Group
* Public

The 3 permission types are:
* Read - Can read the file (shown with a r) (value is +4)
* Write - Can edit the file (shown with a w) (value is +2)
* Execute - Can run the file (shown with a x) (value is +1)

A script file will be labelled name.sh the sh stands for shell which means it can be ran.

```
#!/bin/bash
```
* The universale location of bash on a linux os

```
chmod +x (file_name)
sudo chmod 777 (file_name)
```

* The chmod +x command is an example of adding the excute permission to everyone.
* The chmod 777 command is adding permissions but doing it to a specific code referencing the specfic groups and permission given to each. These can be caluclated here https://chmod-calculator.com/

### System Commands

```
sudo systemctl status (process_name)
sudo systemctl stop (process_name)
sudo systemctl start (process_name)
sudo systemctl restart (process_name)
sudo systemctl enable (process_name)
```
* The systemctl command referes to doing something with one of the processes with the VM.
* status show the current status of the process e.g nginx.
* stop will stop the process if it currently running.
* start will start the process.
* restart will restart the process important if you have changed the config as this won't take effect until it has been restarted.
* enable will allow the process to be automatically started when you start up the instance.

### Varibales and Environment Variables

Variables are your common small scope option that can be used from the directory/space they are located in or by referencing it's path.
Environment variables are on a larger scope and can be ran from anywhere no matter what directory you're located in.

```
printenv
```
* This command shows you the current list of environment variables

```
(variable_name)=(value coule be a number or a strong etc.)
```
* This command will create a variable name and store the data you decide within it


