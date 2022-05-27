import pandas as pd
from FormaDePago import FormaDePago
from Franquicias import Franquicias


class PagoTarjeta1(FormaDePago):

   codigo= str
   banco=str
   Franquicias=Franquicias
   TotalPagar=int
   def __init__(self) -> None:
      super().__init__()
      

   def PagarTarjeta(self,TotalaPagar:int):
      return True

   def CodigoGet(self):
      return self.codigo
   
   def CodigoSet(self,codigo:str):
      self.codigo=codigo

   def BancoGet(self):
      return self.banco

   def BancoSet(self,banco=str):
      self.banco=banco

   def FranquiciaGet(self):
      self.Franquicias
   
   def FranquiciaSet(self,franquicia=Franquicias):
      self.Franquicias=franquicia

   def TotalPagarGet(self):
      self.totalAPagar
   
   def TotalPagarSet(self,total=int):
      self.totalAPagar=total
      

   



      