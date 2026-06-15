#1 Calculate the remainder of two numbers.
print("Calculate the remainder of two numbers.")
a=int(input("Enter a 1st number:"))
b=int(input("Enter a 2nd number:"))
remainder=a%b
print("Remainder:",remainder)

#2 Check if a number is even or odd.
print("Check if a number is even or odd.")
n=int(input("Enter a number:"))
if(n%2==0):
    print("Number is even")
else:
    print("Number is odd")    

#3 Compare two numbers and print the larger one.
print("Compare two numbers and print the larger one.")
x=int(input("Enter a 1st number:"))
y=int(input("Enter a 2nd number:"))
if x>y:
    print("x is larger")
elif y>x:
    print("y is larger")    
else:
    print("Both are equal")    

#4 Write a program to calculate the square and cube of a number.
print("Write a program to calculate the square and cube of a number.")
number=int(input("Enter a 1st number:"))
square=number*number
cube=number*number*number
print("Square of a number is :",square)
print("Cube of a number is : ",cube)

#5 Check if two entered numbers are equal.
print("Check if two entered numbers are equal.")
num1=int(input("Enter a 1st number:"))
num2=int(input("Enter a 2nd number:"))
if num1==num2:
    print("Equal")
else:
    print("Not equal")

#6 Take two numbers and print True if both are positive, else False.
print("Take two numbers and print True if both are positive, else False.")
m=int(input("Enter a 1st number:"))
n=int(input("Enter a 2nd number:"))   
if (m>0 and n>0):
    print("True") 
else:
    print("False")       


#7 Write a program to convert float to integer.
print("Write a program to convert float to integer.")
value=float(input("Enter a value:"))
result=int(value)
print(result)


#8 Take a number as string, convert to int, and multiply by 10.
print("Take a number as string, convert to int, and multiply by 10.")
c=input("Enter a number:")
result=int(c)
print(result * 10)

#9 Write a program that uses and & or operators to check multiple conditions.
print("Write a program that uses and & or operators to check multiple conditions.")
value1=5
value2=10
print(value1>0 and value2>0)
print(value1>0 or value2<0)

#10 Divide two numbers and print the quotient and remainder separately.
print("Divide two numbers and print the quotient and remainder separately.")
n1=int(input("Enter a 1st number:"))
n2=int(input("Enter a 2nd number:"))  
quotient = n1 // n2
remainder =n1%n2
print("Quotient:",quotient)
print("Remainder:",remainder)
