import re
from FormaDePago import FormaDePago

class PagoPse(FormaDePago):
    dispositivo= str
    banco= str
    CorreoElectronico= str


    def __init__(self) -> None:
        super().__init__()


    def BancoGet(self):
      return self.banco

    def BancoSet(self,banco=str):
        self.banco=banco

    def DispositivoGet(self):
        return self.dispositivo

    def DispisticoSet(self,dispositivo=str):
        self.dispositivo=dispositivo

    def CorreoGet(self):
        return self.CorreoElectronico
    
    def CorreoSet(self,correo=str):
        self.CorreoElectronico=correo