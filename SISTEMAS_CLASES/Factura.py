

from Cliente import Cliente
from Persona import Persona
from Empresa import Empresa
from Encabezado import EncabezadoCarritoDeCompras

class Factura:
    precio=int
    Fecha=str
    estado=True
    cliente:Cliente
    Empleado=Persona
    Estado=bool
    empresa=Empresa
    EncabezadoCarritoCompras=EncabezadoCarritoDeCompras

    def __init__(self,empresa1:Empresa,encabezadoCarritoCompras:EncabezadoCarritoDeCompras,cliente:Persona,empleado:Persona):
        
        
        self.EnEncabezadoCarritoCompras=encabezadoCarritoCompras
        self.cliente=cliente
        self.Empleado=empleado
        self.Hora=str
        
        self.empresa=empresa1
        self.Precio=int
        


    def CambiarEstado():
        if ():
            Factura.Estado==True
        



