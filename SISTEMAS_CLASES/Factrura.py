
from Persona import persona
from Empresa import Empresa
from Encabezado import EncabezadoCarritoDeCompras

class Factura:
    Fecha:str
    Hora:str 
    Precio:int
    Cliente:persona
    Empleado=persona
    Empresa=Empresa
    #Estado=bool
    #EncabezadoCarritoCompras=EncabezadoCarritoDeCompras

    def __init__(self,fecha:str):
        #self.estado=True
        self.Fecha=fecha
    ##self.EnEncabezadoCarritoCompras=encabezadocarrito
    ##self.Cliente=cliente    cliente,encabezadocarrito



