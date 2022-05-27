from FormaDePago import FormaDePago
from CarritoDeCompras import CarritoDeCompras

class EncabezadoCarritoDeCompras:
    

    def __init__(self,formaPago:FormaDePago,carritodecompras:CarritoDeCompras):
        self.FormaPago=formaPago
        self.CarritoCompras=carritodecompras
