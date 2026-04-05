#lists
#lists are mutable
numbers = [1,2,3,4]

#CRUD Operations(Create,Read,Update,Delete)
students = ["Hema", "Pavana"] #create
print(students[0]) #Read
students[1] = "Kiran" #Update
print(students[1])
students.remove("Hema")
print(students)

#slicing (used in data processing)
nums = [1,2,3,4,5]
print(nums[1:3])
print(nums[:4])
print(nums[-3:])

#sorting
nums = [2,8,3,5]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

#tuples
#tuples are immutable lists
#for fixed data like coordinates, sensor readings these are used
t = (1,2,3)

#sets (unique values)
a = {"kanna", "nani", "chinni"}
b = {"chinni", "bunny", "sri"}
print(a | b) #union
print(a & b) #intersection

#dictionaries
student = { "name" : "Hema",
           "marks": 90}
print(student["name"])
print(student["marks"])

#nested structures
students = [
    {"name": "Hema", "marks": [90, 85, 88]},
    {"name": "Ravi", "marks": [70, 75, 80]}
]
print(students[0]["marks"][1])  

#JSON (Used in: APIs ,Web apps, Data exchange)
import json

data = {"name": "Hema", "marks": 90}

json_data = json.dumps(data)
print(json_data)