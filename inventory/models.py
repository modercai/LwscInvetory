from django.db import models

# Create your models here.
class Desktop(models.Model):
    model = models.CharField(max_length=25)
    serial_number = models.CharField(max_length=15)
    computer_name = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    year_purchased = models.DateField(blank=True)


    def __str__(self):
        return self.user


class Laptop(models.Model):
    model = models.CharField(max_length=25)
    serial_number = models.CharField(max_length=15)
    computer_name = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    year_purchased = models.DateField(blank=True)

    def __str__(self):
        return self.user



class Printer(models.Model):
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=15,blank=True)
    location =models.CharField(max_length=50)
    year_purchased = models.DateField(blank=True)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.location
    
    
class Server(models.Model):
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    #user name not applicable
    #find out if location is applicable 
    name = models.CharField(max_length=50)
    year_purchased = models.DateField()
    ram = models.CharField(max_length=8)
    storage_capacity = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=25)
    application = models.CharField(max_length=50)
    status = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.model
    
    

