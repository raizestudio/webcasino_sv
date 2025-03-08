from django.db import models


class Continent(models.Model):
    code = models.CharField(max_length=2, primary_key=True)  # ISO 3166-1 alpha-2
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)  # ISO 3166-1 alpha-2
    code_long = models.CharField(max_length=3)  # ISO 3166-1 alpha-3
    code_numeric = models.CharField(max_length=3)  # ISO 3166-1 numeric
    name = models.CharField(max_length=255)  # ISO 3166-1 name
    name_official = models.CharField(max_length=255)  # Official name

    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
