from operator import index
import pandas as pd
from Sucursal import Sucursal

class ArchivoSucursal :

    def GenerarArchivoSucursal(self,sucursal=Sucursal):
        DatosSucursal={"Direccion: ":sucursal.Direccion,"Nombre":sucursal.Nombre,"Direccion":sucursal.Direccion,
        "Cajas: ":sucursal.Cajas}
        df=pd.DataFrame(data=DatosSucursal,index=[0])
        print(df)
        df.to_csv("Archivo Sucursal",index=False)