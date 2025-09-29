# Scopes,Closures and decorators

username = "Chai Aur Code"
def func():
    username = "Chai"
    
# func()
# print(username)


x = 99

def func2(y):
    return x+y

# result = func2(1)
# print(result)


# global keyword is use to acess global variables inside function

# def f1():
#     x = 88
#     def f2():
#         print(f"Inside: {x}")
#     f2()
    
#     print(f"Outside: {x}")
    
# f1()


# closures

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2

# result = f1()
# result()



# def chai(num):
#     def tea(x):
#         return num ** x
    
#     return tea

# result = chai(2)
# updated_result = result(3)
# print(updated_result)


# decorators in Python
# A decorator is a function that takes anothr function as an argument and returns a new function that modifies the behavior of the original function. the new function is reffered to as decorator

def hello():
    print("Hello World!")
    
def greet(fn):
    def mx(a,b):
        print("Good Morning Sir")
        fn(a,b)
        print("Thankyou for using us!")
        
    return mx
    
@greet
def add(a,b):
    print(a+b)
    
add(5,6)