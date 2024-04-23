- [List processes](#list-processes)
- [Kill processes](#kill-processes)
- [Parent, Child and zombie processes](#parent-child-and-zombie-processes)


# List processes

Linux has multiple ways of listing the processes currently running:

* ps - Prints the currently running user processes
* -p <PID> prints the process with the given process id (PID).
* ps -p $$ prints the bash process
* ps aux displays a lot more information and system proceses as a snapshot

* top - Prints the system processes. Similar to ps aux but live. As a result, we can sort by shift+key (e.g. shift+M to sort by memory). Sorts by CPU usage by default.

* jobs - Prints currently running jobs

# Kill processes

We can kill processes from the terminal.

When a process locks up our terminal, there are 3 ways we can free our terminal from the process:

1. q. (Safest)
2. Ctrl-C
3. Ctrl-Z (Unsafe)
   
We can also kill specific processes running on our machine

* kill -x pid - Kills process with pid with kill signal x (default: 15) 
* kill 15 gracefully tries to kill the process by stopping child processes first then the parent ('Terminated')
* kill 9 is brute force kill, harshest possible, could make zombie processes if you kill a parent process ('Killed')

# Parent, Child and zombie processes

A process is a parent process if it spawns another process that is dependant on it. That subprocess is called a child process.

If the parent process is terminated, the child process may not automatically terminate, and so will run until manually terminated. This is called a zombie process.