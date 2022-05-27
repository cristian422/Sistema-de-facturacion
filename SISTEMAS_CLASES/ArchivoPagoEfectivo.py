import pandas as pd
from PagoEfectico import PagoEfectivo1
from FormaDePago import FormaDePago


class ArchivoPagoEfectivo:
    def GenerarArchivo(self,pagoefectivo:PagoEfectivo1):
        DatosPagoEfectivo={"Moneda ":pagoefectivo.moneda}
        df=pd.DataFrame(DatosPagoEfectivo,index=[0])
        print(df)
        df.to_csv("Archivo Pago Efectivo",index=False)