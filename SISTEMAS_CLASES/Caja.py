from numpy import void

class Caja:
    #Empleado: persona
    numero: str
    #factura: factura
    #historial: historial
    def EnviarFactura(Factura) -> True:
        pass
    def VerificarEstado(CarritoDeCompras) -> void:
        pass
from numpy import void

from Persona import Persona
from Factrura import Factura
from Historial import Historial
class Caja:
    Empleado= Persona
    numero= str
    factura:Factura
    historial=Historial

    def __init__(self) -> None:
        pass


    def EnviarFactura() -> True:
        pass

    def verificarEstado(factura:Factura) -> void:

        if(Factura.Estado==True):
            print("La factura se pago con exito: ")
        
        
        
