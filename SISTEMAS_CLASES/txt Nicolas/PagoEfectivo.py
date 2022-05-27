import pandas as pd
from PagoEfectivo import PagoEfectivo1
from FormaDePago import FormaDePago


class ArchivoPagoEfectivo:
    def GenerarArchivo(self,pagoefectivo:PagoEfectivo1):
        df=pd.DataFrame()
        print(df)
        df.to_csv("Archivo Pago Efectivo")