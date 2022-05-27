from UnidadDeMedida import UnidadDeMedida
class Producto:
    Precio:int
    IdProducto:str
    Unidad:UnidadDeMedida

    def __init__(self,precio:int,idProducto=str,unidad=UnidadDeMedida):
        self.Precio=precio
        self.IdProducto=idProducto
        self.Unidad=unidad

    