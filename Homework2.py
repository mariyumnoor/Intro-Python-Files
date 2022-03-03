
"""
Homework # 1
Name: Mariyum Noor
A02346148
"""

#Now, starting with the homework exercises!

#Question 2.3:

"""
Replace *** in the following code with a statement 
that will print a message like 'Congratulations! Your grade of 91 earns you an A in this course'. 
Your statement should print the value stored in the variable grade.
"""

# For user input, we could use this code:
# grade = int (input('To calculate the grade you got, please enter your marks: '))

#Define variable
grade = 91

# Demonstrating an if statement
if grade >= 90:
    print ("Congratulations! Your grade of 91 earns you an A in this course!")

#Else really isn't needed in this because the grade is defined, but I'm doing it anyway!    
else:
    print ("Sorry, you scored lower than 90 so you don't get an A. Better luck next time!")
 
#Print output   
print ("---------------------------------------------")    

#Question 2.4:

"""
(Arithmetic) For each of the arithmetic operators +, -, *, /, // and **, display the
 value of an expression with 27.5 as the left operand and 2 as the right operand
"""

# Demonstrating arithmetic operators

#For +
addition = print (27.5 + 2)

#For - 
subtraction = print (27.5 - 2)

#For *
multiplication = print (27.5 * 2)

#For /
division = print (27.5 / 2)

#For // 
floor_division = print (27.5 // 2)

#For **
exponential = print (27.5 ** 2)

print ("---------------------------------------------")    

#2.5 A

"""
(Circle Area, Diameter and Circumference)

For a circle of radius 2, display the diameter, circumference and area. 

Use the value 3.14159 for π. Use the following formulas
(r is the radius): diameter = 2r, circumference = 2πr and area = πr2. 

[In a later chapter, we’ll introduce Python’s math module which contains a 
higher-precision representation of π.]
"""

#Assign and define variables

r =2 
pie = π = 3.14159

area = pie * (r ** 2)

#Print output 
print ("The area of the circle is: " , area)

print ("---------------------------------------------")    

#2.5 B: Calculating diameter

#Defining variables
r = 2 
pie = π = 3.14159

diameter = 2 * r

#Print output
print ("The diameter of the circle is: " , diameter)

#2.5 Calculating circumference:

#Defining variables
r = 2 
pie = π = 3.14159

circumference = 2 * pie * r
circumference

print ("The circumference of the circle is: " , circumference)

print ("---------------------------------------------")    

#Question 2.6:

"""
(Odd or Even) Use if statements to determine whether an integer is odd or even.
[Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2
leaves a remainder of 0 when divided by 2.]
"""

# Gain user input for the integer

num = int(input("We're trying to determine whether an integer is odd or even. Enter an integer: "))

# We can define a variable with "num = 2 (or any number), but in this instance, we're gaining 
# user input

# Demonstrating an if statement
if num % 2 == 0:
    print(num, "is an even number!")
else:
    print (num, "is an odd number!")  

print ("---------------------------------------------")    


#Question 2.7:

"""
(Multiples) Use if statements to determine whether 1024 is a multiple of 4 and
# whether 2 is a multiple of 10. (Hint: Use the remainder operator.)
"""

# If we want user input we can use:
# num = int(input("We're trying to determine if a number is a multiple of 4. Enter an integer. "))

# But for now, let's define num as 1024 as required in the question:

num = 1024 

# Demonstrating an if statement

if num % 4 == 0:
    print(num, "is a multiple of 4!")
else:
    print (num, "is not a multiple. Better luck next time!")
    
#Is 2 a multiple of 10?

#To gain user input, we can use: num = int(input("Enter an integer. "))

#Defining num as 2:
num = 2

# Demonstrating an if statement
if num % 10 == 0:
    print(num, "is a multiple of 10!")
else:
    print (num, "is not a multiple. Better luck next time!")
    

print ("---------------------------------------------")    

    
'''
Write a script that calculates the squares and cubes
of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use
the tab escape sequence to achieve the three-column output.
'''

#Code if we want to gain input from user: num = int(input("Enter an integer. "))

number = 1

# Demonstrating a "for" statement

for i in range (6):
    squares = i ** 2
    cubes = i ** 3 
    print (i, "\t", squares, "\t" , cubes)
    
    
print ("That's the end of the assignment! :) ")

print ("---------------------------------------------")    



