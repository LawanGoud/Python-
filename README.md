# Intro to Programming with Python

**Software**

Software is a set of instructions to the hardware.

**Programming**

Programming means writing the instructions to create a software.

**Code**

The instructions that we write to create software is called `Code`.

**Syntax**

Similar to Grammar rules in English, Hindi, each programming language has a unique set of rules. These rules are called the **Syntax** of a Programming Language.

## Why Python

Python is an easy to learn, powerful programming language. With Python, it is possible to create programs with minimal amount of code. Look at the code in Java and Python used for printing the message `"Hello World"`

```Java
class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

```Python
print("Hello World")
```

## Applications of Python

Python is a versatile language which has applications in almost every field

- Artificial intelligence (AI)
- Machine Learning (ML)
- Big Data
- Smart Devices/Internet of Things (IoT)
- Cyber Security
- Game Development
- Backend Development, etc.

## Career Opportunities

Python developers have plenty of opportunities across the world

- DevOps Engineer
- Software Developer
- Data Analyst
- Data Scientist
- Machine Learning (ML) Engineer
- AI Scientist, etc.

## Hello World Program in Python

Here is a simple Python code that you can use to display the message `"Hello World"`

```Python
print("Hello World!") # Hello World!
```

## Possible Mistakes

Possible mistakes you may make while writing Python code to display the message "Hello World"

- Spelling Mistake in print

```Python
prnt("Hello World!")
```

- Uppercase ‘P’ in Print

```Python
Print("Hello World!")
```

- Missing quotes

```Python
print(Hello World!)
```

- Missing parentheses

```Python
print("Hello World!"
```

## Printing Without Quotes

If we want to print the numerical result of 2 + 5, we do not add quotes.

```Python
print(2 + 5) # 1
```

If we want to print the exact message `"2 + 5"`, then we add the quotes.

```Python
print("2 + 5") # 2 + 5
```

## Calculations with python

**Addition**

Addition is denoted by `+` sign.
It gives the sum of two numbers.

```Python
print(2 + 5) # 7
print(1 + 1.5) # 2.5
```

## Subtraction

Subtraction is denoted by `-` sign.
It gives the difference between two numbers.

```Python
print(5 - 2) # 3
```

## Multiplication

Multiplication is denoted by `*` sign.

```Python
print(2 * 5) # 10
print(5 * 0.5) # 2.5
```

## Division

Division is denoted by `/` sign.

```Python
print(5 / 2) # 2.5
print(4/2) # 2.0
```

# Coding Practice

## Hello World

### Write a program that prints `Hello World` as output

## Three Hashes

### Write a program that prints three hashes `(###)` as output

---

# Variables and Data Types

## Variables

Variables are like containers for storing values.
Values in the variables can be changed.

## Values

Consider that variables are like containers for storing information.
In context of programming, this information is often referred to as value.

## Data Type

In programming languages, every value or data has an associated type to it known as data type.
Some commonly used data types

- String
- Integer
- Float
- Boolean

This data type determines how the value or data can be used in the program. For example, mathematical operations can be done on Integer and Float types of data.

### String

A String is a stream of characters enclosed within quotes.
Stream of Characters

- Capital Letters ( A – Z )
- Small Letters ( a – z )
- Digits ( 0 – 9 )
- Special Characters (~ ! @ # $ % ^ . ?,)
- Space

Some Examples

- "Hello World!"
- "some@example.com"
- "1234"

**Note**

The Stream of characters enclosed within quotes (`Both single quotes and Double quotes`) are considered as `strings`.

- 'hello'
- "hello"

### Integer

All whole numbers (positive, negative and zero) without any fractional part come under Integers.
Examples

`...-3, -2, -1, 0, 1, 2, 3,...`

### Float

Any number with a decimal point
`24.3, 345.210, -321.86`

### Boolean

In a general sense, anything that can take one of two possible values is considered a Boolean. Examples include the data that can take values like

- True or False
- Yes or No
- 0 or 1
- On or Off, etc.

As per the Python Syntax, `True` and `False` are considered as Boolean values.
Notice that both start with a capital letter.

## Assigning Value to Variable

The following is the syntax for assigning an integer value 10 to a variable age

```Python
age = 10
```

Here the equals to `=`sign is called as **Assignment Operator** as it is used to assign values to variables.

# Coding Practice

## Sum of 2495 and 789358

## subtract 596 from 193856

# Sequence of Instructions

**Program**

A program is a sequence of instructions given to a computer.

## Defining a Variable

A variable gets created when you assign a value to it for the first time.

```Python
age = 10
```

## Printing Value in a Variable

```Python
age = 10
print(age) # 10
```

```Python
age = 10
print("age") # age
```

Variable name enclosed in quotes will print variable rather than the value in it.
If you intend to print value, do not enclose the variable in quotes.

## Order of Instructions

Python executes the code line-by-line.

```Python
print(age)
age = 10 # NameError: name 'age' is not defined
```

Variable age is not created by the time we tried to print.

## Spacing in Python

Having spaces at the beginning of line causes errors.

```Python
a = 10 * 5
b = 5 * 0.5
 b = a + b
```

```Output
File "main.py", line 3
    b = a + b
    ^
IndentationError: unexpected indent
```

## Variable Assignment

Values in the variables can be changed.

```Python
a = 1
print(a) # 1
a = 2
print(a) # 2
```

**Examples of Variable Assignment**

```Python
a = 2
print(a) # 2
a = a + 1
print(a) # 3
```

```Python
a = 1
b = 2
a = b + 1
print(a) # 3
print(b) # 2
```

## Expression

An expression is a valid combination of values, variables and operators.

**Examples**

- a \* b
- a + 2
- 5 \* 2 + 3 \* 4

**BODMAS**

The standard order of evaluating an expression

- Brackets (B)
- Orders (O)
- Division (D)
- Multiplication (M)
- Addition (A)
- Subtraction (S)

```Step by Step Explanation
(5 * 2) + (3 * 4)
(10) + (12)
22
```

```Python
print(10 / 2 + 3) # 8.0
print(10 / (2 + 3)) # 2.0
```

# Coding Practice

## Product of 37, 61 and 391

### Write a program that prints the product of three numbers, 37, 61, 391

## Divide 33968 by 176

### Write a program that prints the result when 33968 is divided by 176.

# Inputs and Outputs Basics

## Working with Strings

## String Contatenation

Joining strings together is called string concatenation.

```Python
a = "Hello" + " " + "World"
print(a) # Hello World
```

## Concatenation Errors

String Concatenation is possible only with strings.

```Python
a = "*" + 10
print(a)
```

```Output
File "main.py", line 1
    a = "*" + 10
    ^
TypeError:
can only concatenate str (not "int") to str
```

## String Repetition

`*` operator is used for repeating strings any number of times as required.

```Python
a = "*" * 10
print(a) # Output: **********
```

```Python
s = "Python"
s = ("* " * 3) + s + (" *" * 3)
print(s) # Output : * * * Python * * *
```

## Length of String

`len()` returns the number of characters in a given string.

```Python
username = input() # Input: Ravi
length = len(username)
print(length) # Output : 4
```

## Take Input From User

- `input()` allows flexibility to take the input from the user.
- `input()` reads a line of input as a string.

```Python
username = input() # Input: Ajay
print(username) # Output: Ajay
```

```Python
username = input() # Input: Ravi
age = input() # Input: 10
print(username + " is " + age + " years old") # Output: Ravi is 10 years old
```

<b>Note</b>

- Even though you **can't** directly **combine strings and integers**, the code works because input() returns a **string**.

- `input()` converts user-entered data (including numbers, booleans, etc) to string. You will learn more about this in further sessions.

- In this case, "10" becomes a string, allowing it to Concatenate and be the part of the final message.

## String Indexing

We can access an individual character in a string using their positions (which start from 0).

These positions are also called as index.

```Python
username = "Ravi"
first_letter = username[0]
print(first_letter) # Output : R
```

## IndexError

Attempting to use an index that is too large will result in an error:

```Python
username = "Ravi"
print(username[4]) # IndexError: string index out of range
```

# Coding Practice - 1A

## Print the Input

Write a program that reads a single line of input and print the given input.

## Print the Input - 2

Write a program that reads a word and prints the word and "###" on two lines.

<b>Note</b> The characters used in "###" are three hash symbols.

## Print the Input - 3

Write a program that reads the two words and prints the two words on two lines

## Second Line

For this problem, you need to write code to read two lines of input and prints the second line of input

## Print in Reverse Order

Write a program that reads two lines of input and prints those two lines in the reverse order. (Print the message given in the second line of input before the first line of input)

## Hello World

Write a program that takes a word W as input and prints "Hello" followed by the given word W.

<b>Note</b> There should be a space after Hello

## Print the Input - 4

For this problem, you need to write code to read a single line of input and print the line after the message "Given Input".

## Join Words

Write a program that reads two words and prints the resultant word by joining the two words.

## Full Name

A job applicant is filling out an application form. He entered his first name and last name. Your task is to print his full name by joining his first name and last name with a space.

## Print Name and Age

Write a program that reads the name and age of a person and prints them in the given format.

# Coding Practice - 1B

## String Repetition

Write a program to print the given input word three times in a single line separated by spaces

## Simple Square

Write a program that prints a simple square using star (\*).

## Simple Square - 2

Write a program that prints a simple square using start(\*).

## Simple Triangle

Write a program that prints a simple triangle using star (\*).

## Simple Triangle - 2

Write a program that prints a simple triangle using star (\*).

## Stars

Write a program that reads a word and prints the word in "\* \* \* word \* \* \*" format.

## First Character

Write a program that reads a word and prints the first character of the word.

## Third Character

Write a program that reads a word and prints the third character of the word.

## First & Last Digits

Given a four-digit number N as input. Write a program to print first and last digit of the number.

## Reverse the digits

Write a program to reverse the digits of a given two-digit number.

# Coding Practice - 1C

## Length of the String

Write a program that reads a word and prints the length of the word.

## Star Repetition

Write a program that reads a word and prints stars(\*) equal to the length of the word.

## Subtract 1 from String Length

Write a program that reads a word and prints `L-1`, where `L` is the length of the word.

## Index of Last Character

Write a program that reads a word and prints the index of the last charcter of the word.

## Last Character

Write a program which prints the last character of a given word.

## Length Excluding Characters

Write a program that reads a word and prints the length of the word excluding the first and last characters

## Star Repetition - 2

Write a program that reads a word and prints the first letter of the given word and stars (\*) instead of the other letters.

## Half Length of String

Write a program that reads a word and prints half the length of the word.

# Assignment - 1A

## Simple Rectangle

Write a program that prints a simple rectangle using stars(\*).

## Simple Square - 3

Write a program that prints a simple square using stars (\*).

## Simple Triangle - 3

Write a program that prints a simple triangle using stars (\*).

## Stars - 2

Write a program that reads a word and prints the word in the given format.

`****** Python ******`

<b>Note</b> The number of stars before and after the word is equal to the length of the word

## Second Word in First Word

write a program that reads two words `W1` and `W2`. `W2` is at the beginning of `W1`

Prints the index at which `W2` ends in `W1`.

## Print in Reverse Order - 2

Write a program that reads two words `A` and `B`, and prints the given words in reverse order separated by `###`

<b>Note :</b> The character used in `###` are three hash symbols.

## First & Last Characters

Write a program that reads a word and prints the first and last characters of the word on two lines.

## First Letters

You are given three strings as input. Write a program to print the first character of each string.

## Star Repetiton - 3

Write a program that reads a string and prints the first and last characters of the given string and prints the stars (`*`) instead of the remaining characters.

# Type Conversion

## String Slicing

Obtaining a part of a string is called string slicing.

<b>Code</b>

```Python
variable_name[start_index:end_index]
```

- Start from the `start_index` and stops at `end_index`
- `end_index` is not included in the slice.

<b>Code</b>

```Python
message = "Hi Ravi"
part = message[3:7]
print(part) # Ravi
```

## Slicing to End

If end index is not specified, slicing stops at the end of the string.

<b>Code</b>

```Python
message = "Hi Ravi"
part = message[3:]
print(part) # Ravi
```

## Slicing from Start

If start index is not specified, slicing starts from the index 0.

<b>Code</b>

```Python
message = "Hi Ravi"
part = message[:2]
print(part) # Hi
```

## Checking Data Type

Check the datatype of the variable or value using `type()`

**Printing Data Type**

```Python
print(type(10)) # <class 'int'>
print(type(4.2)) # <class 'float'>
print(type("Hi")) # <class 'str'>
```

## Type Conversion

Converting the value of one data type to another data type is called _**Type Conversion or Type Casting**_.
We can convert

- String to Integer
- Integer to Float
- Float to String and so on.

## String to Integer

`int()` converts valid data of any type to integer

```Python
a = "5"
a = int(a)
print(type(a)) # <class 'int'>
print(a) # 5
```

## Invalid Integer Conversion

```Python
a = "Five"
a = int(a)
print(type(a))
```

```Output
ValueError:
invalid literal for int() with base 10: 'Five'
```

```Python
a = "5.0"
a = int(a)
print(type(a))
```

```Output
invalid literal for int() with base 10: '5.0'
```

## Adding Two Numbers

```Python
a = input() # Input : 2
a = int(a)
b = input() # Input : 3
b = int(b)
result = a + b
print(result) # Output : 5
```

## Integer to String

`str()` converts data of any type to a string.

**Code**

```Python
a = input() # Input : 2
a = int(a)
b = input() # Input: 3
b = int(b)
result = a + b
print("Sum: " + str(result)) # Output : Sum: 5
```

## Summary

- `int()` -> Converts to integer data type
- `float()` -> Converts to float data type
- `str()` -> Converts to string data type
- `bool()` -> Converts to boolean data type

# Coding Practice - 1D

## Sum of two numbers

Write a program to print the sum of two integers inputs A and B.

## Division of two numbers

Write a program that reads two numbers A and B and prints the division of two numbers (A / B).

## Area of Rectangle

write a program to calculate the area of the Rectangle.

**Note** `Area of Rectangle = Length of Rectangle x Breadth of Rectangle`

## Perimeter of Rectangle

Write a program to calculate the perimeter of a rectangle.

Note: `Perimeter of Rectangle = 2(Length of Rectangle + Breadth of Rectangle)`

## Division of two numbers - 2

Write a program that reads two numbers A and B and prints the division of two numbers (A/B) as an integer.

## Subtraction of two numbers

Write a program that reads two numbers A and B and prints the subtraction of two numbers (A - B).

## Percentage of Boys

Write a program that reads the percentage of girls in a class and prints the percentage of boys in the class.

<b>Note</b> : Total percentage of Boys and Girls in a class is 100.

## Sum of two numbers - 2

Write a program that reads two numbers and prints the sum of two numbers in the given format.

## Kilometers to Meters

Write a program to take the number of kilometers as input and convert into meters and print the number of meters.

<b>Note</b> `1Kilometer = 1000meters`

## Percentage

Write a program that reads a percentage `P` and prints the percentage `P` of the number 200.

## Remainder

Write a program that reads a dividend and a divisor and prints the remainder.

# Coding Practice 1E

## Sum of the digits

Write a program that prints the sum of the digits of a given three-digit number.

## Indexing

Given a word W and a integer N, write a program to print the character present at the index N in the word W.

## String Repetition - 2

Given a word and a number N, write a program to print the given word, N number of times in a single line.

## First Three Characters

Write a program to read a single line of input and print the first three characters in it.

## Part of a String

Write a program that reads a word and an index and prints a part of the word from the given index to the end of the word.

## Part of a String - 2

Write a program that reads a word and two indices (X, Y) and prints a part of the word from the index X to the index Y.

## First N Characters

Write a program that reads a word and a number N and prints the first N characters of the word.

## Last N Characters

Write a program that reads a word and a number N and prints the last N characters of the word

## Second Part of a String

Write a program that reads a string and prints the second part of the string that has digits.

## First Part of a String

Write a program that reads a string and prints the first part of the string that has numbers.

```
`Note`: The given string contains 2 parts

- The first part contains only digits
- The second part contains only one character.
  Example: 10y, 1a
```

# Coding Practice 1F

## Half String

Write a program that reads a string and prints the first half of the string.

## String Repetition 3

Given a word and a number (N), write a program to print the last three characters of the word N times in a single line.

## String Repetition 4

You are given a string. Repeat the same string N times separated by space.

## Star Repetition - 4

Write a program that reads a word and prints the first two and last two letters of the word and prints the stars (\*) instead of the remaining letters.

## Skip the Fourth Character

Write a program that reads a word and prints the word excluding the fourth letter of the word.

## Skipping Letters

You're given a word and an index position of a character. You need to write a program that prints the given word without the character at the given index.

## Simple Square - 4

Write a program that prints a simple square using the hashes (#).

## Simple Triangle - 4

Write a program that prints a simple triangle using the plus (+).

## Stars - 3

Write a program that reads a number N and prints three lines with each line containing N stars (\*)

# Assignment - 1B

## Shape

Write a program that reads a number `N` and prints three lines with each line containing `N` pluses (`+`)

## Basic Arithmetic

Write a program to take two integer inputs (say A and B) and print the result of the following operations.

1. Addition
2. Subtraction
3. Multiplication

## Percentage - 2

Write a program that reads a number N. N is divided into two parts `X` and `Y`.

- `X` is 30 percent of `N`.
- `Y` is the remaining percentage of `N`. Print `Y`.

<b>Note</b>

Total Percentage of X and Y is 100.

The Percentage(P) of Number(N) can be calculated as:

value = (percentage/100) \* number

## Area and Perimeter of Square

You are given a side of square as input. Write a program to find the perimeter and area of the square.

## Star Repetition - 5

Write a program that reads two words `W1` and `W2`.

`W1` contains two parts. The first part contains `W2` and the second part contains the remaining letters in `W1`.

Print `W1` with the first part as start (`*`).

## Part of a String - 3

Write a program that reads a string A and prints the string A by excluding the first two and last two characters of the string.

## Replace a Letter

Write a program that reads a word W, an index I, and a letter C.

Print the word W by replacing the letter at the index I with the given letter C.

## Half String - 2

Write a program that reads a string and prints the second half part of the string.

# Relational Operators

Relational Operators are used to compare values.

Gives `True` and `False` as the result of a comparison.

These are different relational operators

| Operator | Name                        |
| -------- | --------------------------- |
| >        | Is greater than             |
| <        | Is less than                |
| ==       | Is equal to                 |
| <=       | Is less than or equal to    |
| >=       | Is greater than or equal to |
| !=       | Is not equal to             |

```Python
print(5 < 10) # True
print(2 > 1) # True
```

## Possible Mistakes

### Mistake - 1

```Python
print(3 = 3) # SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
```

### Mistake - 2

```Python
print(2 < = 3) # SyntaxError: invalid syntax
```

Space between relational operators `==`, `>=`, `<=` , `!=` is not valid in Python.

## Comparing Numbers

```Python
print(2 <= 3) # True
print(2.53 >= 2.55) # False
```

## Comparing Integers and Floats

```Python
print(12 == 12.0) # True
print(12 == 12.1) # False
```

## Compare Strings

```Python
print("ABC" == "ABC") # True
print("CBA" != "ABC") # True
```

## Case Sensitive

```Python
print("ABC" == "abc") # False
```

- Python is case sensitive.
- It means X (Capital letter) and x (small letter) are not the same in Python.

## Strings and Equality Operator

```Python
print(True == "True") # False
print(123 == "123") # False
print(1.1 == "1.1") # False
```

# Coding Practice - 2A

## Greater than 70

Write a program that reads a number and checks if the given number is greater than 70.

## Greatest among two numbers

Write a program that reads two numbers and checks if the first number is greater than the second number.

<b>Note</b>

Negative numbers are numbers that are less than zero.

## Equal to

Write a program that reads two words and checks if the given two words are the same.

## Sunday

Write a program that reads a day number and checks if the given day is a Sunday.

## Not Equal to

Write a program that reads two numbers and checks if the given two numbers are not the same.

## Greater than or Equal to

Write a program that reads two numbers A and B and checks if A is greater than or equal to B. Print the result as shown in the sample output.

# Coding Practice - 2B

## Greater than - 2

Write a program that reads two numbers A and B and checks if the A is greater than B. Print the result as shown in the sample output.

## Check One Greater

Write a program that reads two numbers A and B, and checks if B is greater than A by one.

## Compare First & Last Letters

Write a program that reads a word and checks if the first lettter and last letter of the word are not the same.

## Compare Sum of the Digits

Write a program that reads a two digit number N. The N consists of only two digits. Check if the sum of the digits of N is greater than 7.

## Validate Password

Write a program to check if the given string is a valid password or not. A string is considered as a valid password if the number of characters present is greater than 7.

## Check Last Part of a String

Write a program that reads two words A and B and checks if the second word B is the last part of the first word A.

## Check Part of a string

Write a program that reads a word A, B, and an index I. Check if B starts at index I in A.

## Compare First Three Characters

Write a program to check if the first three characters in the two given strings are the same.

# Assignment - 2A

## Compare Digits

Write a program that reads a two digit number N and checks,

- if the number N is greater than 25.
- if the first digit of N is greater than the second digit of N.

Print the result as shown in sample output

## Compare First Digit and Last Digit

Write a program that reads two three-digit numbers A and B and checks if the first digit of A is less than the last digit of B.
