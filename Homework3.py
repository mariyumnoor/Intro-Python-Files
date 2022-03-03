
# """
# Homework # 3
# Name: Mariyum Noor
# A02346148
# """

# #Now, starting with the homework exercises!

# ## 3.4

# '''
# (Fill in the Missing Code) In the code below
#       for ***:
#           for ***:
#               print('@')
#           print()
# replace the *** so that when you execute the code, it displays two rows, 
# each containing seven @ symbols, as in:
#       @@@@@@@
#       @@@@@@@
# '''

# #Solution:

# #Creating a for statement
# for i in range(1, 2):
#     for j in range (1, 2):
# #Printing output and multiplying with 7 
#         print('@'*7)
#     print('@'*7)
    

# ## 3.9

# '''
# In Exercise 2.11, you wrote a script that sep- arated a five-digit integer into its individual digits 
# and displayed them. Reimplement your script to use a loop that in each iteration “picks off” one digit 
# (left to right) using the // and % operators, then displays that digit.
# '''
# #create input 
# x = input("Please enter a number which is between 7 to 10 digits: ")

# integer_length = len(x)
# #convert string to integer
# x = int(x)
# #multiply 0 to integer length
# divisor = int('1'+'0'*(integer_length))


# for i in range(1,integer_length+1): #create a for loop
    
#     temp1 = x % divisor #calculate the remainder 
    
#     divisor = round(divisor / 10) 

#     temp2 = temp1 // divisor #calculate the quotient 

#     print(temp2)



# ## 3.11 (Miles Per Gallon) 

# '''
# Drivers are concerned with the mileage obtained by their auto- mobiles. 

# One driver has kept track of several tankfuls of gasoline by recording miles driven and gallons used for each tankful.
# Develop a sentinel-controlled-repetition script that prompts the user to input the miles driven 
# and gallons used for each tankful. The script should calculate and display the miles per gallon obtained
# for each tankful.

# After processing all input information, the script should calculate and
# display the combined miles per gallon obtained for all tankfuls 
# (that is, total miles driven divided by total gallons used).
# '''

# ## 3.11

# Setting variable to zero to start the journey
sum_gallons = 0
sum_miles = 0

#Gaining input from the user for the number of gallons used.
gallons_used = eval(input("Enter the gallons used (Press -1 to end the program)): "))

#Establishing sentinel-controlled-repetition using while statement
while gallons_used != -1:
    #Gaining input from the user
    miles_driven = int(input("Enter the miles driven: "))
    #Adding each input of gallon consumption to calculate the total gallons 
    sum_gallons = sum_gallons + gallons_used
    #Adding each mile to calculate the total miles travelled in the journey
    sum_miles = sum_miles + miles_driven
#Display the miles per gallon obtained for each tankful.
    print("The miles/gallon for this tank was " + str(round(miles_driven/gallons_used, 6)))
    gallons_used = int(input("Enter the gallons used (-1 to end): "))
    
# calculate and display the combined miles per gallon obtained for all tankfuls  
# (that is, total miles driven divided by total gallons used)
print("The overall average miles/gallon used was " + str(round(sum_miles/sum_gallons, 6)))

# ## 3.12 (Palindromes) 

# '''
# A palindrome is a number, word or text phrase that reads the same backwards or forwards. 
# For example, each of the following five-digit integers is a palin- drome: 12321, 55555, 45554 and 11611. 

# Write a script that reads in a five-digit integer and determines whether it’s a palindrome. 

# [Hint: Use the // and % operators to separate the number into its digits.]
# '''

# ## 3.12

# is_a_palindrome = int(input("Hello! Enter any 5-digit number: "))

# # Create a copy of the variable for reversing purposes
# temporary = is_a_palindrome

# # Initating a variable 
# reverse_palindrome=0
# while(is_a_palindrome>0): 

# #Obtain the last digit
#     num=is_a_palindrome%10

# #Create a reverse variable of the palindrome
#     reverse_palindrome=reverse_palindrome*10+num

# #Obtain last digit by floor division
#     is_a_palindrome=is_a_palindrome//10

# #Comparing the reverse palindrome variable to the original temporary variable
# if(temporary==reverse_palindrome):
#     print("Congratulations! This number is a palindrome!")

# else:
#     print("Nopes! Not a palindrome!")
    
# '''
# ## 3.14 (Challenge: Approximating the Mathematical Constant ) 

# Write a script that computes the value of π from the following infinite series. 
# Print a table that shows the value of π approximated by one term of this series, 
# by two terms, by three terms, and so on. How many terms of this series do you have to use before you first get 3.14?
# 3.141? 3.1415? 3.14159?
# '''

# ## 3.14

# #Setting denominator as 1
# denominator = 1
# sum = 0

# #Create a "for" loop 
# for i in range(3000):
    
#     #If iteration is an even number, then we will add to the sum 
#     if i%2 == 0: 
#         sum = sum + 4/denominator
        
#     #If iteration is an odd number, then we will subtract  
#     else:
#         sum = sum - 4/denominator
    
#     #Increasing the denominator by 2 in each loop  
#     denominator = denominator + 2
    
#     #Print out the value of each iteration number
#     print("This is Iteration number: " + str(i)) 
    
#     #Print out the sum 
#     print(sum)
    
# # I see 3.14 twice at Iteration Number 626 and 627
# # I see 3.141 twice at Iteration Number 2453 and 2454