
# variables and data types    single line comment

"""variables    Mulitple Line Comments
AND data types"""

name = "Alice"
age = 30 
height = 5.5
is_student = False
user_data = None

# List
subject = ["Compiler", "Automata", "Os", "DLD", "CCN", "CCNA"]


# list are mutable, meaning their elements can be changed after creation.
# Using curly braces
person = {"name": "Hadi", "age": 24, "role": "Engineer"}
person["name"] = "Salman"  # Modifying an existing value
print(person)
print("Updated Person Name:", person["name"])

# Using the dict() constructor
employee_dict = dict(name="Salman", age=27, role="Manager")

# An empty dictionary
empty_dict = {}



print(type(name))
print("Name:", name)
print(type(age))
print("Age:", age)
print(type(height))
print("Height:", height)
print(type(is_student))
print("Is Student:", is_student)
print(type(user_data))
print("User Data:", user_data)
print(type(subject))
print("Subjects:", subject[2])

print(type(person))
print("Person Dictionary:", person)
print("Person Role:", person["role"])

print(type(employee_dict))
print("Employee Dictionary:", employee_dict)
print("Employee Name:", employee_dict["name"])

