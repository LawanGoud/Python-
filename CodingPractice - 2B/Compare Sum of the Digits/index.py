# Write a program that reads a two digit number N. The N consists of only two digits. Check if the sum of the digits of N is greater than 7.

number = input() # Input: 45

first_digit = int(number[0])
second_digit = int(number[1])

# Convert the input string into two separate digits
sum_of_digits = first_digit + second_digit
# Check if the sum of the digits is greater than 7
result = sum_of_digits > 7
print(result) # Output: True