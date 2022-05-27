from heapq import merge
from operator import index
import pandas as pd
from Factura import Factura
class ArchivosFactura:

    def GenerarArchivoFactrura(self,factura=Factura):
        
        
        DatosFactura={"Cliente : ":factura.cliente.Nombre," cedula ":factura.cliente.Cedula," correo ":factura.cliente.correo," Numero telefonico ":factura.cliente.numeroTelefonico,
        " Hora De la compra ":factura.Hora," Empleado nombre ":factura.Empleado.Nombre," cedula ":factura.Empleado.Cedula,
        " Empresa: ":factura.empresa.sucursal.Nombre," Direccion ":factura.empresa.sucursal.Direccion,
        " precio ":factura.precio," fecha ":factura.Fecha}
        df=pd.DataFrame(data=DatosFactura,index=[0])
        
        print(df)
        df.to_csv("Archivo Factura",index=False)