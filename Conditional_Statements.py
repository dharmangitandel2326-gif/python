#Check if a person is eligible to vote (age ≥ 18).
print("Check if a person is eligible to vote (age ≥ 18).")
age=int(input("Enter age : "))
if age>=18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")    

#Grade calculator based on marks: 90+ = A, 80+ = B, else C.
print("Grade calculator based on marks: 90+ = A, 80+ = B, else C.")
marks=int(input("Enter a marks : "))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
else:
    print("Grade C")    
        
#Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.
print("Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.")
signal = input("Signal : ").lower()

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")    

#ATM withdrawal check: sufficient balance or not.
print("ATM withdrawal check: sufficient balance or not.")
balance=int(input("Enter the amount balance : "))
amount=int(input("Enter withdrawal amount : "))
if amount<=balance:
    print("Withdrawal successfull")
    remaining_balance=balance-amount
    print("Remaining Balance:", remaining_balance)
else:
    print("Insufficient balance")    

#Check if a number is positive, negative, or zero
print("Check if a number is positive, negative, or zero.")
num=int(input("Enter a number:"))
if num>=1:
    print("Positive")
elif num<=-1:
    print("Negative")
else:
    print("Zero")        

#Check if a number lies within a given range.
print("Check if a number lies within a given range.")
limit=25
n = int(input("Enter a number : "))
if n <= limit:
    print("Number is in range")
else:
    print("Number is not in the range")

#Username & password verification.
print("Username & password verification.")
username=input("Enter username: ")
password=input("Enter password: ")
if username == "d@23":
       if password == "2326":
        print("Login successfull")
       else:
        print("Invalid password")
else:
    print("User not found")           
           
#Electricity bill calculator based on units consumed.
print("Electricity bill calculator based on units consumed.")
units=int(input("Enter units : "))
if units<=100:
   bill=units*5
elif units<=200:
    bill=units*7
else:
    bill=units*10
print("BILL :",bill)        


#Simple calculator (add, subtract, multiply, divide).
print("Simple calculator (add, subtract, multiply, divide).")
a=int(input("Enter 1st number : "))
operator = input("Select operation(+,-,*,/) : ")
b=int(input("Enter 2nd number : "))
if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)    
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b) 
else:
    print("Invalid operator")       


#Check type of triangle (equilateral, isosceles, scalene).
print("Check type of triangle (equilateral, isosceles, scalene).")
a=int(input("Enter side a:"))
b=int(input("Enter side b:"))
c=int(input("Enter side c:"))
if a == b == c:
    print("Triangle is equilateral")
elif a==b or b==c or c==a:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")        

       