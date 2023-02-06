from django.db import models

# Create your models here.
class Desktop(models.Model):
    model = models.CharField(max_length=50,null=True,blank=True,)
    serialnumber = models.CharField(max_length=50,unique=True,null=True, blank=True)
    computer_name = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    location = models.CharField(max_length=50,null=True,blank=True,)
    year_purchased = models.CharField(null=True,blank=True, max_length=4,)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user

class Laptop(models.Model):
    model = models.CharField(max_length=50,null=True,blank=True,)
    serialnumber = models.CharField(max_length=50,unique=True,null=True, blank=True)
    computer_name = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    year_purchased = models.CharField(null=True,max_length=4, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user

class Printer(models.Model):
    model = models.CharField(max_length=50)
    serialnumber = models.CharField(max_length=50,unique=True,null=True, blank=True)
    location =models.CharField(max_length=50)
    year_purchased = models.CharField(max_length=4,null=True,blank=True,)
    status = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.location
        
class Server(models.Model):
    model = models.CharField(max_length=50)
    serialnumber = models.CharField(max_length=50,unique=True,null=True, blank=True)
    processor = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    #user name not applicable
    #find out if location is applicable 
    name = models.CharField(max_length=50)
    year_purchased = models.CharField(max_length=4,blank=True,null=True,)
    ram = models.CharField(max_length=8)
    storage_capacity = models.CharField(max_length=50,null=True, blank=True)
    operating_system = models.CharField(max_length=25,null=True, blank=True)
    application = models.CharField(max_length=50,null=True, blank=True)
    status = models.CharField(max_length=50,blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.model
    
    

