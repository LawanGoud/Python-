# Write a program that reads a word A, B, and an index I. Check if B starts at index I in A.

word1 = input() # Input: Repeat
word2 = input() # Input: pea
index = int(input()) # Input: 2

# Check if B starts at index I in A
end_index = index + len(word2)
result = word1[index:end_index] == word2
print(result) # True