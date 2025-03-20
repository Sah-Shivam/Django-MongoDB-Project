from rest_framework import serializers
from .db_connection import person_collection  # Import the existing connection

class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()

    # Custom validation for unique email
    def validate_email(self, value):
        if person_collection.find_one({"email": value}):
            raise serializers.ValidationError("This email already exists. Please use a different email.")
        return value