from django.db import models
import random

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    hotel_name = models.CharField(max_length=255)
    checkin = models.DateField()
    checkout = models.DateField()
    name = models.CharField(max_length=255, default="Unknown")
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    confirmation_number = models.CharField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.confirmation_number:
            self.confirmation_number = self.generate_confirmation_number()
        super().save(*args, **kwargs)

    def generate_confirmation_number(self):
        return f"RES-{random.randint(100000, 999999)}"

    def __str__(self):
        return f"{self.hotel_name} ({self.confirmation_number})"

class Guest(models.Model):
    reservation = models.ForeignKey(Reservation, related_name='guests', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name
