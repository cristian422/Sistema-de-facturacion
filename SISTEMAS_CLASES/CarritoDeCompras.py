from unittest import result
import  Producto
class CarritoDeCompras:
    
    productoSeleccionado=str
    Cantidad=int
    TotalAPagar=int

    def __init__(self,producto:Producto):
        self.ProductoSeleccionado=producto
        self.Cantidad=1
    

    def AumentarCantidad(self):
        cantidad= int (input("cuantos desea agregar: "))
        self.Cantidad=self.Cantidad +cantidad

    def DisminuirCantidad(self):
        cantidad= int (input("cuantos desea eliminar: "))
        self.Cantidad=self.Cantidad +cantidad

    def CalcularTotalProducto(self):
        resultado=int
        self.TotalAPagar=self.ProductoSeleccionado*self.Cantidad


    



    