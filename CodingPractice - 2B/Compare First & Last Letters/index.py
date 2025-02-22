# Write a program that reads a word and checks if the first lettter and last letter of the word are not the same.

word = input() # Input: Python

first_letter = word[0]
last_letter = word[-1]

result = first_letter != last_letter
print(result) # True