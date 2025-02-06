# Write a program that reads a string and prints the first and last characters of the given string and prints the stars (`*`) instead of the remaining characters.

word = input() # Input: qwerty@2020
first_character = word[0]
last_character = word[-1]
stars = "*" * (len(word) - 2)
print(first_character + stars + last_character) # Output: q*********0