from . import serializers
from . import models
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.

def index(request):
    return render(request,"index.html",{})

class BookingView(ModelViewSet):
    queryset=models.Booking.objects.all()
    serializer_class=serializers.BookingSerializer

class MenuView(ModelViewSet):
    queryset=models.Menu.objects.all()
    serializer_class=serializers.MenuSerializer