# Given a word and a number (N), write a program to print the last three characters of the word N times in a single line.

word = input() # Input: Transport
number = int(input()) # Input: 2
last_characters = word[-3:]
print(last_characters * number) # Output: ortort