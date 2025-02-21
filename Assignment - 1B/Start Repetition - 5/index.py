
# Write a program that reads two words `W1` and `W2`.

# `W1` contains two parts. The first part contains `W2` and the second part contains the remaining letters in `W1`.

# Print `W1` with the first part as start (`*`).

word1 = input() # Input: Subway
word2 = input() # Input: Sub

length = len(word2)

first_part = "*" * length
last_part = word1[length:]

print(first_part + last_part) # Output: ***way