from FormaDePago import FormaDePago
from Persona import Persona


class Cliente(Persona):


    def __init__(self, cedula: str, nombre: str,correo: str,numero:str) -> None:
        super().__init__(cedula, nombre)
        self.correo=correo
        self.numeroTelefonico=numero
        

    def Pagar(formadePago:FormaDePago) -> True:
        pass


