# Write a program that reads a word and prints the first letter of the given word and stars (\*) instead of the other letters.

word = input() # Input: Queue
first_character = word[0]
stars = "*" * (len(word) - 1)
print(first_character + stars) # Output: Q****