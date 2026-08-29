# del keyword --> Used to delete object properties or object itself

# class Student:
#   def __init__(self, name):
#     self.name = name

# s1 = Student("Alex")

# del s1.name
# print(s1.name)

# Private(like) attributes & methods
# --> conceptual implementation in Python
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

# class Person:
#   __name = "anonymous"

#   def __hello(self):
#     print("Say Hello!")

#   def welcome(self):
#     self.__hello()

# p1 = Person()

# print(p1.welcome())

# Inheritance --> When one class(child/derived) derives the properties and methods of another class(parent/base).

class Car:
  def __init__(self, type):
    self.type = type

  @staticmethod
  def start():
    print("car started")

  @staticmethod
  def stop():
    print("car stopped")

class ToyotaCar(Car):
  def __init__(self, name, type):
    super().__init__(type)
    self.name = name
    super().start()


class Fortuner(ToyotaCar):
  def __init__(self, type):
    self.type = type

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

# car1 = ToyotaCar("ODI")
# car2 = ToyotaCar("ODI1")
# car1 = Fortuner("diesel")
# car1.start()

# print(car1.start())

# Types of inheritance
# --> Single inheritance
# --> Multi-level inheritance
# --> Multiple inheritance

class A:
  varA = "welcome to class A"

class B:
  varB = "welcome to class B"

class C(A, B):
  varC = "welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

# Super method: super() method is used to access methods of the parent class .

# Class method --> A class method is bound to the class & receives the class as an implicit first argument.

# Note --> static method can't access or modify class state & generally for utility.

class Person:
  name = "anonymous"

  # def changeName(self, name):
  #   self.__class__.name = name

  @classmethod
  def changeName(cls, name):
    cls.name = name

# p1 = Person()
# p1.changeName("kelly")
# print(p1.name)
# print(Person.name)

# Property --> We use @property on any method in the class to use the method as a property .

class Student:
  def __init__(self, phy, chem, math):
    self.phy = phy
    self.chem = chem
    self.math = math

  # def calcPercentage(self):
  #   self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

  @property
  def percentage(self):
    return str((self.phy + self.chem + self.math) / 3) + "%"

# s1 = Student(98, 97, 99)
# print(s1.percentage)

""" 
 Polymorphism --> Operator overloading
              --> When the same operator is allowed to have different meaning according to the context.
 """

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return (22/7) * self.radius ** 2

  def perimeter(self):
    return 2 * (22/7) * self.radius

c1  = Circle(21)

print(c1.perimeter())
print(c1.area())