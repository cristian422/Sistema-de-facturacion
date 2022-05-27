

import pandas as pd
from PagoTageta import PagoTarjeta1


class ArchivoPagoTarjeta:

    def GenerarArchivoPagoTarjeta(self,pagotarjeta=PagoTarjeta1):
        DatosPagotargeta={"Banco ":pagotarjeta.banco,"Codigo: ":pagotarjeta.codigo,"":pagotarjeta.Franquicias,"Total":pagotarjeta.totalAPagar}

        df=pd.DataFrame(data=DatosPagotargeta,index=[0])
        print(df)
        df.to_csv("Archivo Targeta",index=False)