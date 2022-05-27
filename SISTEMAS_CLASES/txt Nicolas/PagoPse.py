from numpy import column_stack
import pandas as pd
from PagoPse import PagoPse1


class ArchivoPagoPse:

    def GenerarArchivo(self,pagopse:PagoPse1):
        DatosPagoPse={"Id del Dispositivo: ":PagoPse1.Dispositivo,"Que banco es:":PagoPse1.Banco,"Cual correo:":PagoPse1.CorreoElectronico}
        df=pd.Data.Frame(data=DatosPagoPse,columns=["Id del dispositivo","Que banco es","Cual correo"],index=[0])
        print(df)
        df.to_csv("Archivo PagoPse")
   