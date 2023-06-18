"""1) Accept two numbers from the user and print 
a) addition 
b) first number squared 2 
c) first number raised to number second number"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1+num2
num1_squared = num1**2
num1_raised_to_num2 = num1**num2
print("Addition of the two numbers is",addition)
print("Square of the first number is:",num1_squared)
print("First number raised to the power of the second number is:",num1_raised_to_num2)
