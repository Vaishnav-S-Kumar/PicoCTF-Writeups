# ABSOLUTE NANO

## Description

You have complete power with nano. Think you can get the flag?

## Solution

Launch the instance and connect to the machine using SSH. Use ```sudo -l``` to view the sudo privileges of the user,it is given the user have 
```
    (ALL) NOPASSWD: /bin/nano /etc/sudoers
```
meaning the user can edit the /etc/sudoers file using nano. Change the following ```/etc/sudoers```-> ```/<file-path>/<file-name>``` 

To use nano to open the file and reveal the flag. 

