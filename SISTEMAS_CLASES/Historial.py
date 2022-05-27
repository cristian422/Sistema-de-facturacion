
from Caja import Caja1
from Persona import Persona

class Historial:
    
    empleadosS= list[Persona]
    hora= str
    fecha= str


    def __init__(self,caja:Caja1) -> None:
        self.caja=caja

    def HoraGet(self):
        return self.hora
    
    def HoraSet(self,hora=str):
        self.hora=hora
    
    def fechaGet(self):
        return self.fecha

    def fechaSet(self,fecha=str):
        self.fecha=fecha
    


