def geeting(name):
    print("Hello, " + name + ". Good morning!")
    
    
# geeting("Alice")
# geeting("Bob")


# print(set({"apple", "banana", "cherry"}))


# Args and Kwargs


def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


# result = sum_numbers(1,2,3,4,5)
# print(result)  # Output: 15


def student_info(**kwargs):
    print("******* Student Information *******")
    for key,value in kwargs.items():
        print(f"Student {key} are: {value}")
    print("***********************************")


# student_info(name = "John", age=22, grade="A")


def find_maximum_number(*args):
    largest_number = None
    for num in args:
        if largest_number is None or largest_number < num:
            largest_number = num
            
    return largest_number



# max_number = find_maximum_number(10, 5, 8, 20, 3,78,95,-789,456)
# print("The maximum number is:", max_number)