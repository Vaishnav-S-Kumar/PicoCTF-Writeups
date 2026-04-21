# Log Hunt

## Description

Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag?

## Solution

Download the log file and use ```grep``` command since we know the flag start with pico.
```
grep -i pico <filename>
```
We can see that a unique word is used, alongside the flag. Use the unique word to find the rest of the flag
```
grep -i <word> <filename>
```


