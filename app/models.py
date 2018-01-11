from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    price = models.IntegerField(max_length=50)
    building = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=4000)

    def __str__(self):
        return self.title