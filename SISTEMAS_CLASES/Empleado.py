from Persona import Persona
class Empleado(Persona):
    Id=str
    def __init__(self, cedula: str, nombre: str,id:str) -> None:
        super().__init__(cedula, nombre)
        self.Id=id
    