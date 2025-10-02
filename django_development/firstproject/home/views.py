from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Client 😎")


def contact(request):
    return HttpResponse("Call Me Mr.x 😈😈")


def dynamic_route(request,number):
    number = int(number)
    print(f"*********** Multiplication Table of {number} ***********")
    for i in range(1,10+1):
        print(f"{i} X {number} = {i * number}")
        
    return HttpResponse("Response by dynamic route!")


def count_alphabets(Request,str):
    count_dict = {}
    
    for char in str:
        if count_dict.get(char):
            count_dict[char] = count_dict[char] + 1
            
        else:
            count_dict[char] = 1
            
            
    for key,value in count_dict.items():
        print(f"{key} count is: {value} times")
        
        
    return HttpResponse("Counting of Allphabest 🤣😂")


def greeting(Request,str):
    name = str[0].upper() + str[1:]
    return HttpResponse(f"Nice to have you back: {name}")