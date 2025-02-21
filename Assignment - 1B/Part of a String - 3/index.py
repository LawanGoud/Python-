# Write a program that reads a string A and prints the string A by excluding the first two and last two characters of the string.

word = input() # Input: ##Soft##
# print(word[2:-2]) # Ouput: Soft

length = len(word)
end_index = length - 2

part = word[2: end_index]
print(part) # Output: Soft