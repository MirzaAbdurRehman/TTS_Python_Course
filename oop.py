# OOPS
# Inheritance

# class Employeee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     def show_info(self):
#         print(self.name, self.salary)

# class Manager(Employeee):
#     def bonus(self):
#         print('Bonus Added')


# m = Manager('Ali',100000)
# m.show_info()
# m.bonus()


# Multilevel Inheritance


# class Grandparent:
#     def house(self):
#         print("Grandparent's house")

# class Parent(Grandparent):
#     def car(self):
#         print("Parent's car")

# class Child(Parent):
#     def bike(self):
#         print("Child's bike")

# c = Child()
# c.house()
# c.car()
# c.bike()


# Multiple Inheritance

# class Father:
#     def skills(self):
#         print("Driving")

# class Mother:
#     def talents(self):
#         print("Cooking")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.skills()
# c.talents()



# Hierarchical Inheritance

# class Shape:
#     def draw(self):
#         print("Drawing shape")

# class Circle(Shape):
#     def circle(self):
#         print("Drawing circle")

# class Square(Shape):
#     def square(self):
#         print("Drawing square")

# c = Circle()
# s = Square()

# c.draw()
# s.draw()





# PolyMorphisim


# class Payment:
#     def pay(self):
#         pass

# class EasyPaisa(Payment):
#     def pay(self):
#         print('Paid Via EasyPaisa')

# class Card(Payment):
#     def pay(self):
#         print('Paid Via Debit Card')

# for method in (EasyPaisa(), Card()):
#     method.pay()



# Encapsulation  Used For Data Hiding


class ATM:
    def __init__(self,pin):
        self.__balance = 10000
        self.__pin = pin

    def checked_balance(self, entered_pin):
        if entered_pin == self.__pin:
            return self.__balance
        else:
            return "Wrong PIN!."
        
atm = ATM(1234)
print(atm.checked_balance(123))