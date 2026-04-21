# Repetitions

## Description

Can you make sense of this file?

## Solution

Download the file and analyse its content after initial analysis, it is found to be base64 encoded text. Therefore to decode, you can use 
```
cat <filename> | base64 -d
```
The result is not a flag and after analysis, It is a base64 enocoded text. So we can assume this is text has been encoded using base64 for multiple times. 
To make the process easier, you can use ```tee``` to display the text as well as write the output to a new file. i.e
```
cat <filename> | base64 -d | tee <new-filename>
```
and continue this process until the flag is displayed.
  
