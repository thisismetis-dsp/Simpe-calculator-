#Bader Alafnan
#A simple chaange made to compare it with my master 
# This python code is written to make a simple Calculator
# Import my classes Calcu
from Calcu import*
# Object/class
calcu1 = clacu()
# print output for users 
print("Please select operation +, -, *, /")
# Take input from the user 
choice = input("Enter operation:  ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#Access methods and variables within the class 
if choice == '+':
   results = calcu1.add(num1,num2)
   print(num1,"+",num2,"=", results)
elif choice == '-':
   results = calcu1.sub(num1,num2)
   print(num1,"-",num2,"=", results)
elif choice == '*':
   results = calcu1.mult(num1,num2)
   print(num1,"*",num2,"=", results)
elif choice == '/':
   results = calcu1.div(num1,num2)
   print(num1,"/",num2,"=", results)
else:
   print("Invalid input")


