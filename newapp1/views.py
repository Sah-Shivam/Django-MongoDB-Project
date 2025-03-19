from django.shortcuts import render
from django.http import HttpResponse  # Correct import for response
from .db_connection import person_collection

# Create your views here.
def index(request):
    return HttpResponse("APP IS RUNNING")

def add_person(request):
    records = {
        "first_name": "arun",
        "last_name": "singh"
    }
    person_collection.insert_one(records)
    return HttpResponse("New person is added")

def get_all(request):
    persons = list(person_collection.find())  # Convert cursor to list
    return HttpResponse(str(persons))  # Display data as string
