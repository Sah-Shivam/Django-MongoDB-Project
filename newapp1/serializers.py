from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):

    # Custom Validation Example
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value

    class Meta:
        model = Person
        fields = '__all__'  # Includes all model fields

    # Default Methods
    def create(self, validated_data):
        """Creates a new Person object"""
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Updates the existing Person object"""
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def to_representation(self, instance):
        """Customize the response structure"""
        data = super().to_representation(instance)
        data['full_name'] = f"{instance.first_name} {instance.last_name}"
        return data
