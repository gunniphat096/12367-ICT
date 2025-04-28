from django.db import models

# Create your models here.
class Person (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + ","+str(self.age)

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    concert = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    seats = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.concert} - {self.date}"
    
class TicketBooking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    concert = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    seats = models.CharField(max_length=255)

    def __str__(self):
        return self.name