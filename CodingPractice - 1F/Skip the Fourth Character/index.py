# Write a program that reads a word and prints the word excluding the fourth letter of the word.

word = input() # Input: Equality
first_part = word[:3]
second_part = word[4:] # This will print the word excluding the fourth letter of the word
print(first_part + second_part) # Output: Equlity