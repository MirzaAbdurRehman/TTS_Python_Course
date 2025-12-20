

# for i in range(17,21):
#     print(i)

# List  get values

# colors = ['black','white','grey','red','indigo','cayan']

# for color in colors:
#     print(color)


# List  get values with index

# colors = ['black','white','grey','red','indigo','cayan']

# for index , color in enumerate(colors):
#     print(f"Index NUmber {index} = {color}")



# Apply For Loop on Multiple at the same time

# colors = ['black','white','grey','red','indigo','cayan','yellow','voilet']

# numbers =[12 ,34,56,78,2,3,57,8]

# for number , color in zip(colors,numbers):
#     print(f"Number {number} = {color}")



# Apply For loop on Dictionary

students = {"name": "Raheem", "age": 17, "isEligible": True}

for key, value in students.items():
    print(key, "=>", type(value))




# while loop infinite loop 

while True:
    select = input('What do you want either (add/ substract/ multiply / quit)')

    if(select == "quit"):
        print("Bye bye!.")
        break
    if(select == "add"):
        print('Addition Mode On!...')
        print('Enter Number_1: ')
        a = int(input())
        print('Enter Number_2: ')
        b = int(input())
        print(f"Sum of a and b = {a+b}")
    elif(select == "substract"):
        print('substraction Mode On!...')
        print('Enter Number_1: ')
        a = int(input())
        print('Enter Number_2: ')
        b = int(input())
        print(f"Sum of a and b = {a-b}")
    elif(select == "multiply"):
        print('multiplication Mode On!...')
        print('Enter Number_1: ')
        a = int(input())
        print('Enter Number_2: ')
        b = int(input())
        print(f"Sum of a and b = {a*b}")
    else:
        print('Invalid Selection')
    



