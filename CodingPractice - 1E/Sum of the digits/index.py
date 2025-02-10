# Write a program that prints the sum of the digits of a given three-digit number.

number = input() # Input: 326

first_digit = number[0]
second_digit = number[1]
third_digit = number[2]

# Convert the input to integers

first_digit = int(first_digit)
second_digit = int(second_digit)
third_digit = int(third_digit)

# Calculate the sum of the digits

sum_of_digits = first_digit + second_digit + third_digit
print(sum_of_digits)