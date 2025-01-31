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
