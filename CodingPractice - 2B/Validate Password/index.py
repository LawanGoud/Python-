# Write a program to check if the given string is a valid password or not. A string is considered as a valid password if the number of characters present is greater than 7.

word = input() # Input: passwd
length = len(word)
is_valid_password = length > 7
print(is_valid_password) # Output: False