
# There are generally 4 Main Pillars of OOPS
# 1. Abstraction
# 2. Polymorphism
# 3. Inheritance
# 4. Encapsulation


class Employee:
    """ This class contains Employee details """

    company_name = "Microprixs Solutions Pvt. Ltd"

    def __init__(self,name,age,gender,designation,salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.designation = designation
        self.__salary = salary
        self.is_married = False


    """ This method gives discription about employee """

    def employee_intro(self):
        return f"Employee Name is {self.name}, {'he' if self.gender == 'male' else 'she'} is {self.age} years old and hold {self.designation} post in the company with monthly salary of {self.__salary}"
    

employee1 = Employee("Arpit",25,"male","Software Developer",35000)
# print(employee1)
# print(employee1.employee_intro())



# PolyMorphism in python

class Circle:
    PI = 3.14
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return f"Ara of Circle is: {self.PI *( self.radius ** 2)}"
    

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return f"Area of Rectangle is: {self.length * self.width}"


def area(shape):
    return shape.calculate_area()


circle = Circle(5)
rectangle = Rectangle(12,13)
# print(area(circle))
# print(area(rectangle))




# Inheritance In Python

class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price


    def intro(self):
        return f"Car Name is: {self.name}, with color of: {self.color} and having price {self.price}"
    

class Car(Vehicle):
    def change_gear(self,number):
        return f"Change gear to {number} of car {self.name}"
    

bmw = Car("Mahindra Thaar","Black",1000000)
# print(bmw.intro())
# print(bmw.change_gear(3))