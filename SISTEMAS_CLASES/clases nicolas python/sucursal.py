import string


class sucursal:
    direccion:string
    nombre_sucursal:string
    cajas:string()
    def__init__(self, direccion:string,nombre_sucursal:string,cajas:string):
        self.direccion:direccion
        self.nombre_sucursal:nombre_sucursal
        self.cajas:string    
            
    def Getdireccion(self):
        return self.direccion
    def Setdireccion(self,direccion):
        self.direccion=direccion
    def Getnombre_sucursal(self):
        return self.nombre_sucursal
    def Setnombre_sucursal(self,nombre_sucursal):
        self.nombre_sucursal=nombre_sucursal
    def Getncajas(self):
        return self.cajas
    def Setcajas(self,cajas):
        self.cajas=cajas
    
