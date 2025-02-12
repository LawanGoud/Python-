# Write a program that reads a string and prints the first half of the string.

word = input() # Input: Amazon
half = len(word) // 2 # Calculate the half of the word
print(word[:half]) # Print the first half of the word