#Take a string input and print its length.
print("Take a string input and print its length.")
student = input("Enter student name: ")
print(len(student))

#Convert a sentence to lowercase.
print("Convert a sentence to lowercase.")
sentence=input("Enter statement:")
print(sentence.lower())

#Replace spaces with underscores in a string
print("Replace spaces with underscores in a string.")
str="I am a coder"
print(str.replace(" ","_"))

#Extract the first and last character of a string.
print("Extract the first and last character of a string.")
string=input("Enter a string:")
print("First character : ",string[0])
print("Last character : ",string[-1])

# Reverse a string using slicing.
print("Reverse a string using slicing.")
str2=input("Enter a string:")
print(str2[::-1])

#Count how many times a letter appears in a string.
print("Count how many times a letter appears in a string.")
fruit="banana"
print(fruit.count("a"))

#Check if a word is present in a sentence.
print("Check if a word is present in a sentence.")
a="I am a coder"
print("am" in a)

#Take name & age and print using f-string formatting.
print("Take name & age and print using f-string formatting.")
name=input("Enter name:")
age=int(input("Enter age: "))
print(f'My name is {name}')
print(f'I am {age} old')

#Remove extra spaces from the start and end of a string.
print("Remove extra spaces from the start and end of a string.")
text= "   Python Programming   "
print(text.strip())

#Join a list of words into a single string with - between them.
print("Join a list of words into a single string with - between them.")
fruits=["apple","banana","mango"]
print("-".join(fruits))

#Create a list of your 5 favorite movies.
print("Create a list of your 5 favorite movies.")
movies=["3 Idiots", "Sita Ramam", "Jab We Met", "Hridayam", "Chhichhore"]
print(movies)

#Add a new movie to the list.
print("Add a new movie to the list.")
movies.append("Brahmastra")
print(movies)

#Remove the first movie from the list.
print("Remove the first movie from the list.")
movies.remove("3 Idiots")
print(movies)

#Sort a list of numbers in ascending order.
print("Sort a list of numbers in ascending order.")
number2=[30,25,46,50,10]
print(number2.sort())

#Reverse a list.
print("Reverse a list.")
movies.reverse()
print(movies)

#Find the largest number in a list.
print("Find the largest number in a list.")
numbers = [10, 25, 7, 45, 18]
print("Largest number : ",max(numbers))

#Merge two lists into one.
print("Merge two lists into one.")
list1=[1,2,3]
list2=[4,5,6]
merged_list=list1+list2
print(merged_list)

#Access the last element of a list without using index number.
print("Access the last element of a list without using index number.")
num=[10,20,30,40,50]
for i in num:
    last=i
print(last)    

#Create a nested list and access a specific inner element.
print("Create a nested list and access a specific inner element.")
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][2])

#Count how many times an element appears in a list.
print("Count how many times an element appears in a list.")
num2=[1,2,3,2,4,5,6,2,7,8,9]
print(num2.count(2))
