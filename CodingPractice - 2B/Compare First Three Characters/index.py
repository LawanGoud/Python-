# Write a program to check if the first three characters in the two given strings are the same.

word1 = input() # Apple
word2 = input() # Application

first_three_chars = word1[:3]
second_three_chars = word2[:3]

are_both_same = first_three_chars == second_three_chars
print(are_both_same) # True