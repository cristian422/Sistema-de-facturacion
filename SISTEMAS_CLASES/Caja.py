from numpy import void
from Persona import Persona
from Factura import Factura

class Caja1:
    empleado : Persona
    factura:Factura
    numero=str
    
    def __init__(self,numero:str) -> None:
        self.numero=numero


    def EnviarFactura() -> True:
        pass

    def verificarEstado(self) -> void:
        if(self.factura.Estado==True):
            print("La factura se pago con exito: ")      
    
    def EmpleadoGet(self):
        return self.empleado

    def FacturaGet(self):
        return self.empleado

    def FacturaSet(self,factura=Factura):
        self.factura=factura

    def NumeroGet(self):
        return self.numero

    
        