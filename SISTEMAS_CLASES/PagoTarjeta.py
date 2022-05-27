import pandas as pd
from FormaDePago import FormaDePago
from Franquicias import Franquicias


class PagoTarjeta1(FormaDePago):
    
    def __init__(self,codigo:str,banco:str,NombreBanco:str,Franquicias:Franquicias) -> None:
       super().__init__()

    def PagarTarjeta(self,TotalaPagar:int):
      codigo: str
      banco:str
      NombreBanco: str
      Franquicias:Franquicias
      

      