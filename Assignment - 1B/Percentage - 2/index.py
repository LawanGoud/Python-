# Write a program that reads a number N. N is divided into two parts `X` and `Y`.

# - `X` is 30 percent of `N`.
# - `Y` is the remaining percentage of `N`. Print `Y`.

number = int(input()) # Input: 50

percent_x = number * (30 / 100)
percent_y = number - percent_x
print(percent_y) # Output: 35.0