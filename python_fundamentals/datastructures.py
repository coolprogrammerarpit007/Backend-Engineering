# Lists in Python

my_list = [23,78,98,78,45,12,67,89]
sorted_list = sorted(my_list)
# print("Sorted List:", sorted_list)

# dictionary in python

student1 = {
    "name":"Abhjeet Gupta",
    "age":20,
    "gender":"Male",
    "courses":["Maths","Physics","Chemistry"],
    "profession":"Student",
    "education":"Engineering",
    "is_married":False
}

# print(student1)

# print("************** Stident Details **************")
# for key,value in student1.items():
#     print(f"Student {key} is {value}")



# print(student1.get("city","Jaipur"))


# Sets Datastructure
# sets are unordered collection of unique items
number_set = {1,2,3,4,5,6,7,8,9,1,2,3,4}
# print(number_set)
friends_set = set(["Arpit","Rajesh"])
# print(friends_set)


# Strings in Python
# Tuples in Python
# Tuples are immutable
# Tuples are ordered collection of items
# Tuples are defined using parentheses ()

planets = ("Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune")


# Programs

def get_largest_number(*args):
    largest_number = None

    for number in args:
        if largest_number is None or largest_number < number:
            largest_number = number

    return largest_number


# largest_number = get_largest_number(78,14,56,98,78,45,65,132,795,-78,20,15)
# largest_number = get_largest_number(-1,-2,-3,-785)
# print(f"Largest Number Is: {largest_number}")


def find_sum(*args):
    total = 0
    for number in args:
        total += number

    return total

# total = find_sum(78,25,12,34,56,78,954)
# print(f"Total Sum Result Is: {total}")


# def reverse_string(str):
#     return str[::-1]

# input_str = input("Enter String: ")
# print(f"Original String IS: {input_str}")
# output_str = reverse_string(input_str)
# print(f"Reversed String Is: {output_str}")


def find_factorial(number):
    fact = 1
    for num in range(1,number+1):
        fact = fact * num

    return fact


# number = int(input("Enter Number: "))
# factorial = find_factorial(number)
# print(f"Factorial of {number} is: {factorial}")

# def letter_case_count(str) -> list[int,int]:
#     upper_count = 0
#     lower_count = 0

#     for ch in str:
#         if ch.isupper():
#             upper_count += 1

#         elif ch.islower():
#             lower_count += 1

#         else:
#             pass

#     return [upper_count,lower_count]

# input_string = input("Enter String: ")
# upper_count,lower_count = letter_case_count(input_string)
# print(f"Upper Case Letters: {upper_count}")
# print(f"Lower Case Letters: {lower_count}")


# def is_pallindrome(str) -> bool:
#     reversed_string = str[::-1]
#     if str == reversed_string:
#         return True
#     return False

# input_string = input("Enter String: ")
# result = is_pallindrome(input_string)
# print(f"String {input_string} is {'Is A Palindrome String' if result else 'Not A Palindrome String '}")

# scope

# a = 5

# def change_value_of_a():
#     global a
#     b = a + 2
#     a = b

#     print(f"Value of a is: {a}")
#     print(f"Value of b is: {b}")


# print(f"Value of a is: {a}")
# change_value_of_a()
# print(f"Value of a is: {a}")