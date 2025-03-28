from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hotel.name} - {self.room_number}"

# Updated Employee model based on assignment requirements
class Employee(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="employees")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

