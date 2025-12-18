

name = "Dawar"
name1 = 'Nusrah'
name2 = ""
name3 = '' 
name4 = '''Mirza Abdur 
Rehman Baig'''
name5 = """Mirza Abdur 
Rehman Baig"""
print(name5)

# String Cocat


greeting = "Hellow" + " " + "Salman"
print(greeting)


# Repition

stars = "*" * 10
print(stars)


# String Methods

message = "    Welcome to Python Programming Language    "
print(message.lower())
print(message.upper())
print(len(message))
print(message.strip())
print(message.replace("Python", "Java"))
print(message.split(" "))


# String Slicing


language = "Python Programming Language"

# 2d
# [start : end]  
# start included
# end excluded
# 1.postive slicing  start with 0  not reverse
# 2.Negative Slicing start -1  reverse
print(language[0:5])  # Python
print(language[4:15])
print(language[-13:-4])

# 3d
print(language[::3])
print(language[::-2])



# Conditional Statement

email = input('Enter Your Email: ').strip().lower()
if "@" not in email:
    print("Inavlid missing '@' sysmbol.")
elif email.endswith("@example.com"):
    print('Company Email Detected!.')
elif email.startswith("admin"):
    print('Admin Email Detected')
else: 
    print('Valid Personal Email.')


# Switch case replace with match case
# how to make funtion

def http_status(status_code):
    match status_code:
        case 200 | 201:
            return "Ok"   
        case 404:
            return "Page Not Found!."
        case 500:
            return "Server Error!."
        case 301 | 302:
            return "Redirect"
        case _ if status_code >= 400:
            return "Client or Server Error!..."
        case _:

            return "Unknown Status"

print(http_status(404)) 
