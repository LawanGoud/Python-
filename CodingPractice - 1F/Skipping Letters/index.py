# You're given a word and an index position of a character. You need to write a program that prints the given word without the character at the given index.

word = input() # Input: Combine
index = int(input()) # Input: 4
first_part = word[:index]
second_part = word[index + 1:]
print(first_part + second_part) # Output: Combine