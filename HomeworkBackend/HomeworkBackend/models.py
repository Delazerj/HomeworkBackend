from django.db import models


class Country (models.Model):
    name = models.TextField()

    def __str__(self): return self.name


class Snowboarder (models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    date_of_birth = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self): return self.first_name + " " + self.last_name

