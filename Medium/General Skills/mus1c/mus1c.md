# mus1c

## Description

I wrote you a song. Put it in the picoCTF{} flag format. 

Hint: Do you think you can master rockstar?

## Solution

Download the txt file contatining the lyrics and analyse it, It basically makes no sense. Then understand what the hint means.

After looking for sme reference, It is clear that rockstart is a programming language that uses song lyrics as syntax. ie instead of using ```print``` it uses ```shout```. So, every syntax used has a some reference to music. 

To use this language there is a online interpreter called ```rockstar online interpreter```, where you paste the lyrics in the txt file and run the program. 

As result, we get a bunch of numbers, which indicate it is decimal and using decimal to ASCIII conversion (Just search Decimal to ASCIII and use any online tool) we get the content of the CTF flag.
