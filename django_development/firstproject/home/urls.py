
from django.urls import path
from home.views import index,contact,dynamic_route,count_alphabets,greeting,client_html,friends

urlpatterns = [
    path('home/',index),
    path('contact/',contact),
    path('dynamic-route/<int:number>/',dynamic_route),
    path('count-alphabets/<str>',count_alphabets),
    path('greetings/<str>',greeting),
    path('client/',client_html),
    path('friends/',friends)
]