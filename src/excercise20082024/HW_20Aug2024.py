

"""
Task 7 - Leap year checker
Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.
"""
y = int(input("Enter the year: \n"))
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("This is a leap year")
else:
    print("Not a leap year")

"""
Task 8 - Triangle classifier
Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.
"""
n1 = int(input("Enter 1st sides of triangle: "))
n2 = int(input("Enter 2nd sides of triangle: "))
n3 = int(input("Enter 3rd sides of triangle: "))
if n1 == n2 and n1 == n3:
    print("Equilateral")
#elif (n1 == n2 and n1 != n3) or (n2 == n3 and n2 != n1) or (n1 == n3 and n1 != n2):
elif n1 == n2 or n2 == n3 or n3==n1:
    print("Isoscelless")
else:
    print("Scalene")

"""
Task 9
 FizzBuzz Test:

Write a program that prints numbers from 1 to 100. # Loop For

However, for multiples of 3, print "Fizz" instead of the number, and

for multiples of 5, print "Buzz."

For numbers that are multiples of both 3 and 5, print "FizzBuzz."
"""

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz",end = ' ')
    elif i%5==0:
        print("Buzz",end=" ")
    elif i%3==0:
        print("Fizz",end=" ")
    else:
        print(i,end=" ")


