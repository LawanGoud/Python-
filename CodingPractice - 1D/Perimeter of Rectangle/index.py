# Write a program to calculate the perimeter of a rectangle.

length = input() # Input: 3
breadth = input() # Input: 4

# Convert the input to integers
length = int(length)
breadth = int(breadth)

# Calculate the perimeter of the rectangle
perimeter = 2 * (length + breadth)
print(perimeter) # Output: 14