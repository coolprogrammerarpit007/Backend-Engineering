# print("My name is Arpit Mishra!")
# print("I am learning Python.")

# Operators in Python
# Arithmetic Operators: +, -, *, /, %, //, **
# Comparison Operators: ==, !=, >, <, >=, <=
# Logical Operators: and, or, not  
# Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=
# Bitwise Operators: &, |, ^, ~, <<, >>
# Membership Operators: in, not in
# Identity Operators: is, is not    

first_number = 5
exponential_first_number = first_number ** 3
# print(exponential_first_number)

sentence = "This course is taught by Abhijeet Gupta Sir"
# print("Abhijeet" in sentence)  # True


num1 = 5
num2 = 5
# print(num1 is num2)  # True

# Identity operators in Python are used to check whether two variables refer to the same object in memory, not just whether their values are equal. The main identity operators are is and is not

# This prints True because in Python, small integers (usually from -5 to 256) are interned (cached and reused) to optimize memory and speed. Whenever a variable is assigned such a value, Python refers to the same object in memory for that value. Therefore, n1 and n2 both point to the same memory location where the integer 2 is stored, so n1 is n2 evaluates to True

num3 = 785
num4 = 785
# print("Testing identity operators in Python")
# print(num3 is num4)  # False


# Pratice Problems on Conditional Statements in Python
# Problem 1: Write a program to check whether a number is deivsible by 3 or not

# number = int(input("Enter a number: "))
# if number % 3 == 0:
#     print(f"The Number {number} is divisible by 3")
# else:
#     print(f"The Number {number} is not divisible by 3")

# Problem 2: whether number is even or odd
# if number % 2 == 0:
#     print(f"The Number {number} is Even")
# else:
#     print(f"The Number {number} is Odd")

# Problem 3: Check whether a person is eligible to vote or not
# age = int(input("Enter your age: "))
# if age > 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")


# Write a program for greeting a person

# username = input("Enter your name: ").strip()
# if username.lower() == "arpit":
#     print("Hello Arpit! You are the admin of this system")
# else:
#     print(f"Hello {username}! Welcome Abroad It is nice to have you here")


# current_year = int(input("Enter Year in YYYY format: "))

# if current_year % 100 == 0:
#     if current_year % 400 == 0:
#         print(f"The Year {current_year} is a Leap Year")
#     else:
#          print(f"The Year {current_year} is not a Leap Year")
    
    
# elif current_year % 4 == 0:
#     print(f"The Year {current_year} is a Leap Year")
    
# else:
#     print(f"The Year {current_year} is not a Leap Year")

# Problem 5: Program to check whether a number is positive, negative or zero
# number = int(input("Enter a number: "))
# if number > 0:
#     print(f"The Number {number} is Positive")
# elif number < 0:
#     print(f"The Number {number} is Negative")
# else:
#     print(f"The Number is Zero")


# check whether a char is vowel or consonant
# char = input("Enter a character: ").strip().lower()

# if char in ['a','e','i','o','u']:
#     print(f"Entered character {char} is a Vowel")
# else:
#     print(f"Entered character {char} is a constant")


# Program to find if ther user entered correct password or not
# correct_password = "abc@123"
# user_password = input("Enter Your Password: ").strip()

# if user_password == "":
#     print("Password can not be empty!")
# elif user_password == correct_password:
#     print("You have successfully logged in!")
# else:
#     print("You have entered wrong password!")



