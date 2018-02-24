from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
from django.http import HttpResponse
from .custom.Greeting import Greeting
from .custom.Messaging import CustomError, Message
from .custom.Utils import DateUtil

# $.ajax({url:"/api/rest/hello/", data:{"name":"Jorge"}, dataType: "json" })

def hello(request   ) :
    try:
        greeting = Message("returning salutation","success",Greeting(request.GET['name']))
    except MultiValueDictKeyError:
        greeting = CustomError("The path you've just reached is correct but a parameter must be provided in order to send the appropriate salutation")

    return HttpResponse(greeting.toJSON())

def time(request):
    date = DateUtil()
    return HttpResponse("{{ data: {{ shortDate: {0}, fullDate: {1} }} }}".format(date.shortDate, date.fullDate))

def whosthere(request):
    return HttpResponse(CustomError('This is a test of the CustomError class').toJSON())
