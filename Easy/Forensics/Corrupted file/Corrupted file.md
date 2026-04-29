# Corrupted file

## Description

This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?

## Solution 

Download the file and use the ```file``` command to print what type of file it is. 
Use the ```string``` command to print readable characters from the file, the first word is JFIF which stands for JPEG File Interchange Format meaning it is a jpeg file. Maybe some bytes are wrong as mentioned in the description meaning if the bytes are corrected, the original file would displayed.

Use the ```hexeditor``` tool to view hex/byte order of the file. Cross check the magic number of JFIF with the hex values of the file and change the value of the hex accordingly.
 
