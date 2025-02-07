# Write a program that reads two numbers and prints the sum of two numbers in the given format.

a = input() # Input: 3.0
b = input() # Input: 4.0

# Convert input to floats
a = float(a)
b = float(b)
# Calculate the sum of two numbers
sum = a + b
# convert sum to string
sum_str = str(sum)

print("Sum: " + str(sum_str)) # Output: Sum: 7.0