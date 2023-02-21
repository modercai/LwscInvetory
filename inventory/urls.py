from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('desktops',views.all_desktops,name='list-desktops'),
    path('laptops',views.all_laptops,name='list-laptops'),
    path('servers',views.all_servers,name='list-servers'),
    #searching a device
    path('search_printer',views.search_printers,name='search-printers'),
    path('search_desktop',views.search_desktops,name='search-desktops'),
    path('search_laptop',views.search_laptops,name='search-laptops'),
    path('search_server',views.search_servers,name='search-servers'),
    #printers
    path('printers',views.all_printers,name='list-printers'),
  
    
    
    
]