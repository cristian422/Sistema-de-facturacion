import pandas as pd
from Factrura import Factura
class ArchivosFactura:

    def GenerarArchivoFactrura(self,factura=Factura):

        DatosFactura={"Cliente: ":factura.Cliente,"Hora De la compra":factura.Hora,"Empleado":factura.Empleado,
        "Empresa:":factura.Empresa,"precio":factura.Precio,"fecha":factura.Fecha}
        
        df=pd.DataFrame(data=DatosFactura,columns=["Cliente","Hora De la compra","Empleado","Empresa","precio","fecha"],index=[0])
        print(df)
        df.to_csv("Archivo Factura")