from enum import Enum
import pandas as pd
from PagoTarjeta import PagoTarjeta1
from FormaDePago import FormaDePago

class ArchivoPagoTarjeta(Enum):

    def GenerarArchivoPagoTarjeta(self,pagotarjeta=PagoTarjeta1):
         DatosPagoTargeta={"Codigo de la tarjeta: ":PagoTarjeta1.Codigo,"Tipo de Banco":PagoTarjeta1.Banco,"Nombre de Banco":PagoTarjeta1.Banco,}
        