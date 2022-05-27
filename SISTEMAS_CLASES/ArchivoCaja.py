from turtle import pd
from Caja import Caja1

import pandas as pd
class ArchivoCaja:

    def GenerarArchivo(self,caja=Caja1):
        DatosCaja={"Numero de la caja":caja.numero}
        df=pd.DataFrame(DatosCaja,index=[0])
        print(df)
        df.to_csv("Archivo Caja",index=False)