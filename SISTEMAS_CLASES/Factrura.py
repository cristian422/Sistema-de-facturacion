

from Cliente import Cliente
from Persona import Persona
from Empresa import Empresa
from Encabezado import EncabezadoCarritoDeCompras

class Factura:
    Fecha:str
    Hora:str 
    Precio:int
    cliente:Cliente
    Empleado=Persona
    Empresa:Empresa
    Estado=bool
    #EncabezadoCarritoCompras=EncabezadoCarritoDeCompras

    def __init__(self,fecha:str):
        self.estado=True
        self.Fecha=fecha
        self.EnEncabezadoCarritoCompras=EncabezadoCarritoDeCompras
        self.cliente    

    def CambiarEstado():
        if ():
            Factura.Estado==True
        



