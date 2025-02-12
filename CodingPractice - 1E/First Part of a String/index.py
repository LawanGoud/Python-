# Write a program that reads a string and prints the first part of the string that has numbers.

word = input() # Input: 10y
no_of_characters = len(word)
index = no_of_characters - 1
number = int(word[:index])
print(number) # Output: 10