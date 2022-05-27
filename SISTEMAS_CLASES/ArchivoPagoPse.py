
import pandas as pd
from PagoPse import PagoPse



class ArchivoPagoPse:

    def GenerarArchivo(self,pagopse:PagoPse):
        DatosPagoPse={"Banco":pagopse.banco,"dispositivo":pagopse.dispositivo}
        df=pd.DataFrame(data=DatosPagoPse,index=[0])
        print(df)
        df.to_csv("Archivo PagoPse",index=False)