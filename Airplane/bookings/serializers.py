from rest_framework import serializers
from .models import Flight, Passenger

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'  # Include all fields in the Flight model

class PassengerSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)  # Include flight details in the passenger serializer

    class Meta:
        model = Passenger
        fields = '__all__'  # Include all fields in the Passenger model

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
