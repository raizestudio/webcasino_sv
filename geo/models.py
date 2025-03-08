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

class AdministrativeLevelPrimary(models.Model):
    code = models.CharField(max_length=10, primary_key=True)  # ISO 3166-2
    name = models.CharField(max_length=255)
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AdministrativeLevelSecondary(models.Model):
    code = models.CharField(max_length=10, primary_key=True)  # ISO 3166-2
    name = models.CharField(max_length=255)

    primary = models.ForeignKey(AdministrativeLevelPrimary, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class CityManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('primary', 'secondary')
    
class City(models.Model):
    name = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    
    primary = models.ForeignKey(AdministrativeLevelPrimary, on_delete=models.CASCADE, related_name='cities', null=True, blank=True)
    secondary = models.ForeignKey(AdministrativeLevelSecondary, on_delete=models.CASCADE, related_name='cities', null=True, blank=True)

class Street(models.Model):
    name = models.CharField(max_length=255)
    
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Address(models.Model):
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=255)
    floor = models.CharField(max_length=10)
    door = models.CharField(max_length=10)
    
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.street}, {self.number}, {self.floor}, {self.door}"