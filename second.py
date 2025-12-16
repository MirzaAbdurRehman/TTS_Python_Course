
# Tuples are immutable, meaning their elements cannot be changed after creation.

# tuple_1 = (1, 2, 3, 4, 5,"Abid")  
# tuple_1[1] = 10  # This will raise a TypeError


# list are mutable, meaning their elements can be changed after creation.

subject = ["Compiler", "Automata", "Os", "DLD", "CCN", "CCNA",12.3]
subject[1] = "Data Science"  # This is valid
print("Modified Subjects List:", subject)

single = (10,)


# Sets are unordered collections of unique elements. Mutable

students = {"Ali","Ahmed","ahmed","Sara","Ali","Zara"}
students.add("Omar")
students.remove("Sara")
print("Students Set:", students)


numbers = [1,23,4,5,3,2,1,4,5,3,2,4,6,7,8,9,7,6,5,4,3,2,1]
unique_numbers = set(numbers)
print("Unique Numbers Set:", unique_numbers)




# Type Conversion

# 10.0 + 20.5
a,b,c,d = 10, 20.5, "30", "40.5"   
print("Sum: ", a + b)
print("Sum: ", (b) + float(d))
print("Sum: ", a + int(c))


# User Input

print("Enter First Number: ")
num_1 = float(input())
print("Enter Second Number: ")
num_2= float(input())
print("MULITPICATION: ", num_1 * num_2)

