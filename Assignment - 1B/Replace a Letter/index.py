# Write a program that reads a word W, an index I, and a letter C.

# Print the word W by replacing the letter at the index I with the given letter C.

word = input() # Input: Prime
index = int(input()) # Input: 3
letter = input() # Input: z

first_part = word[:index]
last_part = word[index + 1:]

print(first_part + letter + last_part) # Output: Prize


# Another Approach

# # Convert the word to a list of characters
# word_list = list(word)
# # Replace the character at the index with the given letter
# word_list[index] = letter
# # Convert the list back to a string
# print(''.join(word_list)) # Output: Priz

