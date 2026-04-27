# Binary Search 

## Description

Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses. Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!

## Solution

Download the zip file to find analyse the code which runs the program, after analysis it is clear that the program uses binary search and it is clear that the instance is going to ask the user to guess a number between 0 and 1000, which means a 1000 possibilities but the user is only given 10 guesses. 

```
Binary Search is an algorithm for finding an element in a sorted collection. 
Instead of checking every element one by one, it repeatedly divides the search space in half, which makes it much faster than linear search for large datasets.
The algorithm relies on the idea that the data is already sorted. Without this condition, binary search cannot determine which half of the data to discard, and its efficiency advantage disappears.
i.e consider an array of values between 0 and 10, the target is 7. instead of going through 0,1,2 etc. The program divides the array and compares the value of the target with middle value.
If the middle value equals the target, the search ends. If the target is smaller than the middle value, the search continues in the left half by updating the end to mid − 1. If the target is larger, the search continues in the right half by updating the start to mid + 1. This process repeats until the element is found or the range becomes empty.
```
So basically to get right answer within 10 guess we need to be the algorithm, start by entering 500 (1000/2) if it higher, use 750 (middle value between 500 and 1000), if lower, use 250 (middle value between 0 and 500), thus continue the cycle. 
