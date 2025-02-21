# Write a program that reads a string and prints the second half part of the string.

word = input() # Input: Football

length = len(word)
second_half = word[length//2:]
print(second_half) # Output: ball