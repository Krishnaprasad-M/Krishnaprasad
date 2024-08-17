"""Task #3

-a. Explain the difference between the = operator and the == operator in Python.

- b.What does the ** operator do in Python, and how is it used?

- c.What does the ^ operator do in Python, and in what context is it commonly used?"""
import math
"""
#a.
# = - Assignment operator, used for assigning literal values to variables/identifiers
#== - Relational operator used    for checking equality between 2 values

#b.** - used for exponentiation (a**b)
#c.Used for power only"""
### Task #4

#- Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)
r = int(input("Enter the radius: \n"))
pi=math.pi
print(f"The value of pi is {pi}")
area = pi*(pow(r,2))
print(f"The area is {area:.2f}")
#------------------------------------------------------------------------------------
"""
### Task #5
- Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
"""
a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
if a>b:
    print(f"The first number {a} is greater than second number {b}")
elif b>a:
    print(f"The first number {a} is less than second number {b}")
else: print(f"The first number {a} is equal to second number {b}")

"""
### Task #6

- Develop a Python script that calculates the square and cube of a given number.
"""
n = int(input("Enter your value: "))
print(f"The Square of {n} is {pow(n,2)} and the cube of {n} is {pow(n,3)}")

