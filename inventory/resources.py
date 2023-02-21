from import_export import resources
from .models import Desktop
from .models import Laptop
from .models import Printer
from .models import Server


class DesktopResource(resources.ModelResource):
    class meta:
        model = Desktop
        
class LaptopResource(resources.ModelResource):
    class meta:
        model = Laptop

class PrinterResource(resources.ModelResource):
    class meta:
        model = Printer
        
class ServerResource(resources.ModelResource):
    class meta:
        model = Server