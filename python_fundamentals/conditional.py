# # Conditional Statements

name1 = "Alice"
name2 = "Alice"
# print(name1 is name2)  # True, because both refer to the same string object

# number = int(input("Enter a number: "))
# print(f"********* Table of {number} **********")
# for index in range(1,11):
#     print(f"{number} X {index} = {number * index}")

# for index in range(10,0,-1):
#     print(index)
    
# print("Counting Upto 10")
# for index in range(1,11):
#     print(f"Conunt Upto {index}")
    
# else:
#     print("Completed Upto 10")

# print("Calculate Square upto a given range: ")
# start_number = int(input("Enter Starting Number: "))
# end_number = int(input("Enter Ending Number: "))

# for number in range(start_number,end_number+1):
#     print(f"Square of {number} is {number ** 2}")
    
# else:
#     print("Completed Calculation of Squares")


# While Loops in Python

# start_number = int(input("Enter Starting Number: "))
# end_number = int(input("Enter Ending Number: "))

# print("Counting from Start to End in reverse order")
# while end_number >= start_number:
#     print(f"Number is: {end_number}")
#     end_number -= 1
    
# else:
#     print("Completed Counting in reverse order")



# print(f"Starting from {start_number} to {end_number}")
# while start_number <= end_number:
#     print(f"Number is: {start_number}")
#     start_number += 1
    
# else:
#     print("Completed Counting in normal order")


# start_number = int(input("Enter Starting Number: "))
# end_number = int(input("Enter Ending Number: "))

# while start_number <= end_number:
#     print(f"********* Table of {start_number} **********")
#     for index in range(1,11):
#         print(f"{start_number} X {index} = {start_number * index}")
        
#     print("*******************************")
#     start_number += 1




# str = " "
# name = input("Enter Name: ")
# number = int(input("Enter a number between 1 to 10: "))
# for index in range(0,number):
#     str += name + " "
    
# index = 0
# while index < number:
#     print(str)
#     index += 1

# Break,Continue and Pass Statements in Python

# Number Guessing Game
import random
secret_number = random.randint(1,101)
print(f"Secret Number is: {secret_number}" )  # For testing purpose, 
max_guesses = 5

while True:
    user_guess = int(input("Enter your guess between 1 to 100:  "))
    if user_guess == secret_number:
        max_guesses -= 1
        print("Congratulations! you guessed it right!")
        print("You Win!")
        print(f"Secret Number was: {secret_number}, you guessed it right when you still have {max_guesses} guesses left!")
        break
    
    elif user_guess < secret_number:
        print("Try a higher number!")
        max_guesses -= 1
        continue
    
    elif user_guess > secret_number:
        print("Try a lower number!")
        max_guesses -= 1
        continue
    
    else:
        print("Invalid Input, Please try again!")
        max_guesses -= 1
        continue
    
    
else:
    print("You have completed all your gusseses!")
    print("You Lose!")
    print(f"Secret Number was: {secret_number}")