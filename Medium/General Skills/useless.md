# useless 

## Description

There's an interesting script in the user's home directory

## Solution

Launch the instance and connect to the machine using SSH. 

After connecting, use ```pwd``` to print the current directory name and use ```ls``` to list the files in the direcotry. Use the ```cat``` command to view the program source code.
```
#!/bin/bash
# Basic mathematical operations via command-line arguments

if [ $# != 3 ]
then
  echo "Read the code first"
else
        if [[ "$1" == "add" ]]
        then 
          sum=$(( $2 + $3 ))
          echo "The Sum is: $sum"  

        elif [[ "$1" == "sub" ]]
        then 
          sub=$(( $2 - $3 ))
          echo "The Substract is: $sub" 

        elif [[ "$1" == "div" ]]
        then 
          div=$(( $2 / $3 ))
          echo "The quotient is: $div" 

        elif [[ "$1" == "mul" ]]
        then
          mul=$(( $2 * $3 ))
          echo "The product is: $mul" 

        else
          echo "Read the manual"
         
        fi
fi
```

One thing that stood out is the else statement, "Read the manual". There is no manual (file) created in associtation with this program but the ```man``` command can be used to view the manual [This command is used for viewing the manual of commands]. i.e ```man <filename>``` which shows manual of the program along with the flag.
