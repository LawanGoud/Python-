# Write a program that reads a word and prints the first two and last two letters of the word and prints the stars (\*) instead of the remaining letters.

word = input() # message
first_two = word[:2] # first two letters
last_two = word[-2:] # last two letters
stars = "*" * (len(word) - 4)
print(first_two + stars + last_two) # print first two letters