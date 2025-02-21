# Write a program that reads two numbers A and B and checks if A is greater than or equal to B. Print the result as shown in the sample output.

a = input()
a = float(a) # Input: 4.3
b = input()
b = float(b) # Input: 3.2

result = a >= b
result = str(result)

print("A >= B is " + result) # Output: A >= B is True