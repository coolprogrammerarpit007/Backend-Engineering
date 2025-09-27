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


