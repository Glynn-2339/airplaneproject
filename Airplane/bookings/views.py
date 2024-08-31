from django.shortcuts import render
from django.http import HttpResponse

# from django.shortcuts import redirect
# Create your views here.
from rest_framework import viewsets
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

def homepage(request):
    return HttpResponse("<h1>Welcome to the Airline Booking System API</h1><p>Use the API at <a href='/api/'>/api/</a></p>")

# def redirect_to_admin(request):
#     return redirect('/admin/')

def homepage(request):
    return render(request, 'bookings/homepage.html')

