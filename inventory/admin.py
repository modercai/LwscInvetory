from django.contrib import admin
from . models import  Desktop
from .models import Laptop
from .models import Printer
from .models import Server

# Register your models here.

admin.site.register(Desktop)
admin.site.register(Laptop)
admin.site.register(Printer)
admin.site.register(Server)