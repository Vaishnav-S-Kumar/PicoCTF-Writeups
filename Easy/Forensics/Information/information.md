# Information

## Description

Files can always be changed in a secret way. Can you find the flag?

## Solution

Download the image file and view the image to see if the flag is displayed within the file.

Use Exiftool to view the metadata. The license setion of the metadata views a base64 encoded text. Decode the base64 text to get the flag.

