
class Sucursal:
    
    Cajas:str
    Direccion=str
    Nombre=str

    def __init__(self,direccion:str,nombre:str):
        self.Direccion=direccion
        self.Nombre=nombre
    
    def CajasGet(self):
        return self.Cajas

    def CajasSet(self, cajas=str):
        self.Cajas=cajas
        return self.Cajas
    
    def DireccionGet(self):
        return self.Direccion
    
    def DireccionSet(self,direccion=str):
        self.Direccion=direccion

    def NombreGet(self):
        return self.Direccion
    
    def NombreSet(self,direccion=str):
        self.Direccion=direccion


