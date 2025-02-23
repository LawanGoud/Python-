# Write a program that reads a two digit number N and checks,

# - if the number N is greater than 25.
# - if the first digit of N is greater than the second digit of N.

# Print the result as shown in sample output

number = input() # Input: 28

is_greater_than_25 = int(number) > 25

is_first_digit_greater_than_second = int(number[0]) > int(number[1])

print(is_greater_than_25) # Output: True
print(is_first_digit_greater_than_second) # Output: False