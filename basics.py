#1. Write a program to print your name, age, and city in one line. 
name=input("Enter name:")
age=int(input("Enter age:"))
city=input("Enter city:")
print("Name:", name, "Age:", age, "City:", city)


#2. Take user input for two numbers and print their sum. 
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Sum:",num1+num2)


#3. Write a program to convert temperature from Celsius to Fahrenheit. 
C=int(input("Enter temperature in Celsius:"))
F=(C*9/5)+32
print(f'{C} in Fahrenheit is {F}')


#4. Store your name in a variable and print it in uppercase. 
name=input("Enter name:")
print(name.upper())

#5. Ask the user for their birth year and calculate their current age. 
birth_year=int(input("Enter birthyear:"))
current_age=2026-birth_year
print("CURRENT AGE:",current_age)


#6. Write a program to swap the values of two variables. 
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
temp=a
a=b
b=temp
print("After swapping:")
print(a)
print(b)

#7. Create a program to calculate the area of a rectangle from user inputs. 
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print("Area of Rectangle:", area)

#8. Write a program to check if a number is positive or negative.
x=int(input("Enter number:"))
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

#9. Ask for two numbers and print their average.
m=int(input("Enter first number:"))
n=int(input("Enter second number:"))
print("Average:",(m+n)/2)