# Generators in python

# Generator is a simple type of Iterator that allows you to generate values one at a time, instead of creating and storing the entire sequence in memory
# They are memory efficient
# they are defined using functions with the yield keyword

# 🔹 Difference Between Normal Function and Generator

# A normal function uses return → it ends immediately when return is hit.
# 
# A generator function uses yield → it "pauses" and can continue from where it left off.

# Example 1 Simple generator


def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))


# generators for squares

def square_numbers(num):
    for i in range(num):
        yield i*i

# squares = square_numbers(5)

# for number in squares:
#     print(number)


# Using Generator Expressions

# Instead of writing a generator function, you can use generator expressions (similar to list comprehensions, but with () instead of []):

squares = (x*x for x in range(5))


# for val in squares:
#     print(val)


# 🔹 Why Use Generators?

# ✅ Memory Efficient → Useful for large datasets (no need to store entire list).
# ✅ Lazy Evaluation → Generates values on demand.
# ✅ Pipeline Processing → Can chain generators for data processing.



# Memory Efficient

import sys

# List Comprehensions

numbers1 = [x*x for x in range(1,2000)]
print(f"List Size: {sys.getsizeof(numbers1)}")


# Generator Expressions
numbers2 = (x*x for x in range(1,2000))
print(f"Generator Memory Size: {sys.getsizeof(numbers2)}")


doubled = list(map(lambda x:x*x,numbers2))
print(doubled)



# decorator

def greeting(fn):
    def mx():
        print("Good Morning! Nice to Meet You")
        fn()
        print("It was nice meeting you, see you soon")

    return mx


@greeting
def hello():
    print("Hello World!")


hello()