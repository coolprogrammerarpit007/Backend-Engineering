# collections in python

# Collections is a built in Python module that provide useful collection data-types. Container data-types allow you to access and store values in the convenient way

# Improve Code Readability : namedtuple()
# planets = ("Earth","Mars","Venus")
# print(planets[0])


# namedtuple is an enhanced version of tuples, the key difference b/w namedtuple and tuple is that In tuple you access value using indices whereas In namedtuple you access it by names

# you can conveniently define what attributes a namedtuple can hold and create multiple instances of It so In terms of functionality it is much closer to class


# creating a namedtuple which represents movie with attributes genre,rating,actor

from collections import namedtuple

# attribute values are passed as string separated with ' '

movie = namedtuple('movie','genre rating actor')


# crating instances of tuples

ironman = movie(genre="SuoerHero",rating=9.9,actor="Robert Downey Junior")
titanic = movie(genre="Romance",rating=8.7,actor="Leonardo Decaprio")


# Access the fileds

# print(titanic.genre)
# print(titanic.rating)
# print(titanic.actor)


# Why use namedtuple over dictionary

# 1. A namedtuple takes less memory space compared to dictionary, so In case of large data namedtuple is much better

# book_dict = {"author":"JK Rowling","name":"Harry Potter and Chamber Of Secrets","pages":567,"price":2500}
# book = namedtuple('book',['author','name','pages','price'])
# book1 = book(**book_dict)
# # print(book1)

# book2 = book1._replace(pr ice=7500)
# # print(book2)

from collections import Counter

numbers = [1,75,887,75,1,1,75,887,23,75,95,887,1]
num_counter = Counter(numbers)
# print(num_counter)s

#counter with strings
string = 'lalalalandismagic'
string_count = Counter(string)
# print(string_count)

# Using counter on sentences
line = 'he told her that her presentation was not that good'

list_of_words = line.split() 
line_count=Counter(list_of_words)
# print(line_count)

most_common_word = Counter(list_of_words).most_common(1)
# print(most_common_word)


# defaultdict in collection module


from collections import defaultdict

# def_dict = defaultdict(object)
def print_default():
    return 'value absent'

def_dict=defaultdict(print_default)
# print(def_dict['chocolate'])
def_dict['fruit'] ="Apple"
def_dict['drink'] = "CokeCola"
# print(def_dict)
# print(def_dict['chocolate'])


# create a dict and print items
vehicle = {'bicycle': 'hercules', 'car': 'Maruti', 'bike': ' Harley', 'scooter': 'bajaj'}

# print('This is normal dict')
# for key,value in vehicle.items():
#     print(key,value)

# print('-------------------------------')

# # Create an OrderedDict and print items
# from collections import OrderedDict
# ordered_vehicle=OrderedDict()
# ordered_vehicle['bicycle']='hercules'
# ordered_vehicle['car']='Maruti'
# ordered_vehicle['bike']='Harley'
# print('This is an ordered dict')

# for key,value in ordered_vehicle.items():
    # print(key,value)


# When a key is deleted, the information about its order is also deleted. When you re-insert the key, it is treated as a new entry and corresponding order information is stored.


# UserList in the collections module


from collections import UserList


# class user_list(UserList):

#     # method to raise error on Insertion
#     def append(Self,s=None):
#         raise RuntimeError("Authority denied for the new Insertion")
    
# my_list = user_list([11,22,33,44,55])

# try:
#     my_list.append(95)

# except RuntimeError:
#     print("Some Runtime Error Occurs")



# from collections import UserString

# class user_string(UserString):
#     def append(self,new):
#         self.data = self.data + new

#     def remove(self,s):
#         self.data = self.data.replace(s, "")


# text='apple orange grapes bananas pencil strawberry watermelon eraser'
# fruits = user_string(text)

# for word in ['pencil','eraser']:
#     fruits.remove(word)

# print(fruits)

from collections import UserDict 
my_dict={'red':'5','white':2,'black':1} 

# Creating an UserDict 
user_dict = UserDict(my_dict) 
print(user_dict.data) 

# Creating a Dictionary where deletion of an  is not allowed 
class user_dict(UserDict):       
    # Function to stop delete/pop
    def pop(self, s = None):
        raise RuntimeError("Not Authorised to delete") 

data = user_dict({'red':'5','white':2,'black':1}) 

# try to delete a item
data.pop(1)