# from django.shortcuts import render
# from django.http import HttpResponse  # Correct import for response
# from .db_connection import person_collection

# # Create your views here.
# def index(request):
#     return HttpResponse("APP IS RUNNING")

# def add_person(request):
#     records = {
#         "first_name": "arun",
#         "last_name": "singh",
#         "age":52,
#         "email":"arum@ww.com"
#     }
#     person_collection.insert_one(records)
#     return HttpResponse("New person is added")

# def get_all(request):
#     persons = list(person_collection.find())  # Convert cursor to list
#     return HttpResponse(str(persons))  # Display data as string




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client['mydatabase']
person_collection = db['persons']

class PersonAPI(APIView):

    # GET: Retrieve all persons
    def get(self, request):
        persons = list(person_collection.find({}, {"_id": 0}))  # Exclude MongoDB's ObjectID
        return Response({"persons": persons}, status=status.HTTP_200_OK)

    # POST: Add new persons
    def post(self, request):
        serializer = PersonSerializer(data=request.data, many=isinstance(request.data, list))

        if serializer.is_valid():
            if isinstance(request.data, list):
                person_collection.insert_many(serializer.validated_data)
            else:
                person_collection.insert_one(serializer.validated_data)

            return Response({"message": "Person(s) added successfully!"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
