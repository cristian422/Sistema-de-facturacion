from FormaDePago import FormaDePago
from CarritoDeCompras import CarritoDeCompras

class EncabezadoCarritoDeCompras:
    FormaPago=FormaDePago
    CarritoCompras=CarritoDeCompras

def __init__(self,formaPago:FormaDePago,carritodecompras:CarritoDeCompras):
    self.FormaPago=formaPago
    self.CarritoCompras=carritodecompras
