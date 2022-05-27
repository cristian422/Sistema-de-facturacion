import pandas as pd
from Historial import Historial

class ArchivoHistorial:

    def GenerarArchivoHistorial(self,historial=Historial):
        DatosHistorial={"hora":historial.hora,"fecha":historial.fecha}
        df=pd.DataFrame(data=DatosHistorial,index=[0])
        print(df)
        df.to_csv("Archivo historial",index=False)