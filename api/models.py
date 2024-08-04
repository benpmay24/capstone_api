from django.db import models

# Create your models here.

class Booking(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    no_of_guests=models.IntegerField()
    bookingdate=models.DateTimeField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    ID=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=255)
    price=models.FloatField()
    inventory=models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'




