from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "name: " + self.name + ", model: " + self.model + ", year: " + str(self.year) + ", price: " + str(self.price)

class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    color = models.CharField(max_length=255) 

    def __str__(self):
        return "Car: " + str(self.vehicle) + ", color: " + self.color

class Bus(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    passenger_capacity = models.IntegerField()

    def __str__(self):
        return "Bus: " + str(self.vehicle) + ", Passenger Capacity: " + str(self.passenger_capacity)
