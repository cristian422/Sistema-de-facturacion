import pandas as pd
from Producto import Producto

class ArchivoProducto:

    def GenerarArchivo(self,producto=Producto):
        DatosProducto={"IdProducto":producto.IdProducto,"Precio ":producto.Precio,"Unidad":producto.Unidad}
        df=pd.DataFrame(DatosProducto)
        print(df)
        df.to_csv("Archivo Producto")