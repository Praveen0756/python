# OOP --> Object Oriented Programming .
# To map with real world scenarios, we started using objects in code. This is called object oriented programming.

# Class --> class is a blueprint for creating objects.
# class Student:
#   #default constructor
#    def __init__(self):
#    print("adding new student in DB...")
#    Class & Instance Attributes
#   college_name = "ABC college" # --> class attribute

#   def __init__(self, name, marks):
#     self.name = name # --> instance object
#     self.marks = marks

# #Methods --> methods are functions that belong to objects.
#   def welcome(self):
#     print("Welcome student")

#   def get_marks(self):
#     return self.marks

# creating object is instance of class

# s1 = Student("Jack")
# print(s1.name)
# print(s1.name)

# class Car:
#     color= "red"
#     brand = "BMW"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# __init__ Function --> "Constructor", All classes have a function called __init__(), which is always executed when the object is being initiated

# Self --> The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to that class.

""" --------------------------------------------------------- """


# Q1 - Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def get_average(self):
    sum = 0
    for el in self.marks:
      sum += el
    print("Hi", self.name, "your avg score is:", sum/3)

# Static Methods: Methods that don't use the self parameter(work at class level)
# Decorators --> Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

  @staticmethod # --> Decorator
  def hello():  # --> Static method
    print("Hello")

# s1 = Student("Jack", [99, 98, 97])
# s1.get_average()

""" --------------------------------------------------------- """

# Abstraction --> Hiding the implementation details of a class and only showing the essential features to the user.

# Encapsulation --> Wrapping data and functions into a single unit(object).

class Car:
  def __init__(self):
    self.acc = False
    self.brk = False
    self.clutch = False

  def start(self):
    self.clutch = True
    self.acc = True
    print("Car started")


# car1 = Car()
# car1.start()

""" --------------------------------------------------------- """

# Q2 --> Create Account class with 2 attributes - balance and account no. , Create methods for debit, credit and printing the balance

class Account:
  def __init__(self, bal, acc):
    self.balance = bal
    self.account_no = acc

  def debit(self, amount):
    self.balance -= amount
    print("Rs.", amount, "was debited")
    print("Total balance = ", self.get_balance())

  def credit(self, amount):
    self.balance += amount
    print("Rs.", amount, "was credited")
    print("Total balance = ", self.get_balance())

  def get_balance(self):
    return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
