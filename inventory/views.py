from django.shortcuts import render
from .models import Desktop, Laptop, Printer, Server

# Create your views here.
def home(request):
    desktop_count = Desktop.objects.all().count()
    laptop_count = Laptop.objects.all().count()
    printer_count = Printer.objects.all().count()
    server_count = Server.objects.all().count()
    return render(request, 'inventory/home.html',{'desktop_count':desktop_count,'laptop_count':laptop_count,'printer_count':printer_count,'server_count':server_count},)

def all_desktops(request):
    desktop_list = Desktop.objects.all()
    desktop_count = desktop_list.count()
    return render(request,'inventory/desktops.html',{'desktop_list':desktop_list,'desktop_count':desktop_count})

def all_laptops(request):
    laptop_list = Laptop.objects.all()
    return render(request,'inventory/laptops.html',{'laptop_list':laptop_list})

def all_printers(request):
    printer_list = Printer.objects.all()
    return render(request,'inventory/printers.html',{'printer_list':printer_list})



def all_servers(request):
    server_list = Server.objects.all()#change the name server here and in models.py to something else.
    return render(request,'inventory/servers.html',{'server_list':server_list})

#views for searching devices

def search_printers(request):
    if request.method == "POST":
        searched_printer = request.POST['searched_printer']
        printers = Printer.objects.filter(serialnumber__contains=searched_printer)
        return render(request,'inventory/printers.html',{'searched_printer':searched_printer,'printers':printers,})
    else:
        return render(request,'inventory/printers.html',{})
    
def search_desktops(request):
    if request.method == "POST":
        searched_desktop = request.POST['searched_desktop']
        desktops = Desktop.objects.filter(serialnumber__contains=searched_desktop)
        return render(request,'inventory/desktops.html',{'searched_desktop':searched_desktop,'desktops':desktops,})
    else:
        return render(request,'inventory/desktops.html',{})
    
    
def search_laptops(request):
    if request.method == "POST":
        searched_laptop = request.POST['searched_laptop']
        laptops = Laptop.objects.filter(serialnumber__contains=searched_laptop)
        return render(request,'inventory/laptops.html',{'searched_laptop':searched_laptop,'laptops':laptops,})
    else:
        return render(request,'inventory/laptops.html',{})
    
def search_servers(request):
    if request.method == "POST":
        searched_server = request.POST['searched_server']
        servers = Server.objects.filter(serialnumber__contains=searched_server)
        return render(request,'inventory/servers.html',{'searched_server':searched_server,'servers':servers,})
    else:
        return render(request,'inventory/servers.html',{})


#counting the numbe of items in the database
    
#def desktopCount(request):
    #count= Desktop.objects.all()
    #return render(request, 'inventory/home.html', {'count': count})
    
    
    
# make a check for the search and determine the appropriate response.
# remove the search bar from the navigation bar and make the navigation bar look beautiful.
    
   