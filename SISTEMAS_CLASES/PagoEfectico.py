import pandas as pd
from FormaDePago import FormaDePago
class PagoEfectivo1(FormaDePago):
    moneda=str
    def _init_(self) -> None:
        super()._init_()
        self.moneda=str
    
    def PagarEnEfectivo(TotalPagar:int):
        return True
    
    def MonedaGet(self):
        return self.moneda

    def MonedaSet(self,moneda=str):
        self.moneda=moneda