## Compare First Digit and Last Digit

# Write a program that reads two three-digit numbers A and B and checks if the first digit of A is less than the last digit of B.

a = input() # Input: 123
b = input() # Input: 378

first_digit = int(a[0])
last_digit = int(b[-1])

result = first_digit < last_digit
print(result) # True