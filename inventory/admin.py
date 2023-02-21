from django.contrib import admin
from .models import  Desktop
from .models import Laptop
from .models import Printer
from .models import Server
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Desktop)
class DesktopAdmin(ImportExportModelAdmin):
    list_display = ('model', 'serialnumber', 'computer_name' ,'user', 'location',  'year_purchased',  'active',)
@admin.register(Laptop)
class LaptopAdmin(ImportExportModelAdmin):
    list_display = ('model', 'serialnumber', 'computer_name' ,'user', 'location',  'year_purchased',  'active',)
@admin.register(Printer)
class PrinterAdmin(ImportExportModelAdmin):
    list_display = ('model', 'serialnumber', 'location' ,'year_purchased', 'status','active',)
@admin.register(Server)
class ServerAdmin(ImportExportModelAdmin):
    list_display = ('model', 'serialnumber', 'processor' ,'speed', 'name',  'year_purchased',  'ram','storage_capacity','operating_system','application','status','active',)