import pandas as pd
from Persona import Persona
class ArchivoPersona:

    def GenerarArchivo(self,persona=Persona):
        DatosPersona={"Nombre :":persona.Nombre,"Cedula: ":persona.Cedula}
        df=pd.DataFrame(DatosPersona,index=[0])
        print(df)
        df.to_csv("Archivo Persona",index=False)