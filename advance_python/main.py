# Advance Python Concepts

# List:- lists are ordered,mutable and allows duplicate items

my_list = ['banana','apple','oranges','grapes']
my_list.insert(0,'BlueBerry')
# print(my_list)

vegetable_list = ['Potato','Tomatos','Onions','Cabbage']
shopping_list = vegetable_list + my_list
# print(shopping_list)



# num1 = 78
# num2 = 78

# print(num1 is num2)
# print(f"Number 1: {num1} and Number 2: {num2}")
# num1 = 39
# print(f"Number 1: {num1} and Number 2: {num2}")



# List Comprensions


numbers = [1,2,3,4,5,6,7,8,9,10]
square_numbers = [number ** 2 for number in numbers]
# print(numbers)
# print(square_numbers)



# Tuples in Python
# Tuples are ordered, immutable and allow duplicate items

# planets = ("EARTH","MOON","MARS","VENUS","JUPYTER")
# for planet in planets:
#     print(f"Planet Name: {planet}")
    
    
# reversed_planets = planets[::-1]
# print(reversed_planets)

# planet1,*args,planet2 = planets
# print(planet1)


# Dictionary:- These are key-value pairs,unordered and mutable
student = {
    'name':"Arpit",
    'age':25,
    'gender':'Male',
    'is_married':False
}



# Sets in python
# sets are unordered,mutable and not allowed duplicates


number_set = {1,2,3,4,5,6,7,8,9,10}