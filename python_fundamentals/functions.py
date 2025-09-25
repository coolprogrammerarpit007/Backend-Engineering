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


