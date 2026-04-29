# Extensions

## Description

This is a really weird text file. Can you find the flag? Get the flag from TXT.

## Solution

Download the txt file and use cat to see the contents of the file(it is full of gibberish), use the file command to find the orginal file type
```
file filename.txt              
filename.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```
Which means the file is originally a png file, so to retrieve the file we upload the file to cyberchef.io to render the image or we can change the file extension .txt to .png, either way works.

