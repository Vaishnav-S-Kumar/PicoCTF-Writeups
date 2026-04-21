# MultiCode

## Description

We intercepted a suspiciously encoded message, but it’s clearly hiding a flag. No encryption, just multiple layers of obfuscation. Can you peel back the layers and reveal the truth?

## Solution

Download the message file and use CyberChef(https://gchq.github.io/CyberChef/). Pass the message/content to its inout field

After analysing the text, we can undertand the last layer of enoding used was base64, thus use ```From base64``` after which use ```From Hex``` to convert the result.

The string of character after the above procedure is a URL encoded string, URL decode option break the next level of encoding. Still the flag is not shown. 

Analyse the latest result, It uses a ROT13 encoding. Use the ROT13 option to bring orginal flag
