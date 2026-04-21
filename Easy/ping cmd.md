# Ping CMD

## Description

Can you make the server reveal its secrets? It seems to be able to ping Google DNS, but what happens if you get a little creative with your input?

## Solution

Launch the instance and connect usingg ```nc```/ NetCat. After connecting it is shown
```
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 
```
so enter 8.8.8.8 and see if it pings. Yes, it does and automatically closes the connection. 

Connect once again and instead of just 8.8.8.8, use ```| ls``` after the IP and see the result.

This is called command injection or more specifically OS Command Injection. It is technique which takes user input and directly passes it to the operating system shell, allowing an attacker to execute unintended system commands.

Using the ```` | cat <filename>``` after the IP, you can read the flag. For bonus, you can read the program file which is also available and understand how the machine works.
