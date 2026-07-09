#Create a tuple with 5 numbers.
print("Create a tuple with 5 numbers.")
numbers=(1,2,3,4,5)
print(numbers)

#Access the third element in a tuple.
print("Access the third element in a tuple.")
numbers=(1,2,3,4,5)
print(numbers[2])

#Unpack a tuple into separate variables.
print("Unpack a tuple into separate variables.")
numbers=(1,2,3,4,5)
a,b,c,d,e = numbers
print(a,b,c,d,e)
print(a)

#Create a set of 5 fruits.
print("Create a set of 5 fruits.")
fruits={"apple","mango","banana","kiwi","strawberry"}
print(fruits)

#Add a new fruit to the set.
print("Add a new fruit to the set.")
fruits.add("orange")
print(fruits)

#Remove an element from a set.
print("Remove an element from a set.")
fruits.remove("mango")
print(fruits)

#Find union of two sets.
num1 = {1,2,3}
num2 = {3,4,5}
print(num1 | num2)

#Find intersection of two sets.
num1 = {1,2,3}
num2 = {3,4,5}
print(num1 & num2)

#Check if one set is subset of another.
print("Check if one set is subset of another.")
s1={1,2,3}
s2={1,2,3,4,5,6}
print(s1.issubset(s2))

#Convert a list with duplicate values into a set to remove duplicates.
print("Convert a list with duplicate values into a set to remove duplicates.")
numbers=[1,2,3,1,2,3,4,5]
print(set(numbers))

#Create a dictionary storing student names and marks.
student={
   "Harry":67,
   "Riya":70,
   "Ron":56,
   "John":40,
   "Tom":89
}
print(student)

#Add a new key-value pair to an existing dictionary.
print("Add a new key-value pair to an existing dictionary.")
student["Aris"]=36
student["Leo"]=76
print(student)

#Delete a key-value pair from a dictionary.
print("Delete a key-value pair from a dictionary.")
student.pop('John')
print(student)

#Merge two dictionaries into one.
print("Merge two dictionaries into one.")
student1={
    "Joe":53,
    "Helly":66,
}
student2={
    "Krishi":78,
    "Astha":56
}
student={**student1,**student2}
print(student)

#Check if a key exists in a dictionary.
print("Check if a key exists in a dictionary.")
stu={
    "name":"Dhami",
    "age":"18",
}
key=input("Enter a key:")
if key in stu:
    print("Key exists")
else:
    print("Key does not exist")

#Count word frequency in a given string using a dictionary.
print("Count word frequency in a given string using a dictionary.")   
fruits= "apple banana orange apple kiwi apple kiwi banana"
words=fruits.split()
counter={}
for word in words:
    counter[word]=counter.get(word,0) +1
print(counter)

#Find the key with the maximum value in a dictionary.
print("Find the key with the maximum value in a dictionary.")
marks={
    "Science" : 65,
    "Maths" : 89,
    "English" : 92
}
print(max(marks,key=marks.get))

#Reverse keys and values in a dictionary.
print("Reverse keys and values in a dictionary.")
student={
    "name" : "Dharmangi",
    "age" : 20
}
reverse = {}
for key in student:
    reverse[student[key]] = key
print(reverse)

#Update the value for a specific key.
print("Update the value for a specific key.")
student["name"] = "Dhami"
print(student)

#Convert a list of tuples into a dictionary.
print("Convert a list of tuples into a dictionary.")
data = [("name" , "Dharmangi"),("age" , 20),("course" , "CSE")]
student = dict(data)
print(student)