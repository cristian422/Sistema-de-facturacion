
import re
from Producto import Producto
class CarritoDeCompras:
    
    productoSeleccionado:Producto
    Cantidad=int
    TotalAPagar=int

    def __init__(self,producto:Producto):
        self.roductoSeleccionado=producto
        self.Cantidad=1
    

    def AumentarCantidad(self):
        cantidad= int (input("cuantos desea agregar: "))
        self.Cantidad=self.Cantidad +cantidad

    def DisminuirCantidad(self):
        cantidad= int (input("cuantos desea eliminar: "))
        self.Cantidad=self.Cantidad +cantidad

    def CalcularTotalProducto(self): 
        print (self.Cantidad)
        print(self.productoSeleccionado.Precio)
        self.TotalAPagar=self.Cantidad* self.productoSeleccionado.Precio
    
        return print("regreso")


    def ProductoSeleccionado(self):
        return self.productoSeleccionado
    
    def Catidad(self):
        return self.Cantidad
    
    def ToTalAPagar(self):
        return self.TotalAPagar
        
        


    



    