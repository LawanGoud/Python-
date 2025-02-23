# Write a program that reads two words A and B and checks if the second word B is the last part of the first word A.

word1 = input() # Blackhole
word2 = input() # hole

length = len(word2)

last_part = word1[-length:]

result = last_part == word2
print(result) # True