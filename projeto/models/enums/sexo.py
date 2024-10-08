from enum import Enum

class Sexo(Enum):

    MASCULINO = ("Masculino", "M")
    FEMININO  = ("Feminino", "F") 

    def __init__(self, caractere, texto) -> None:

        self.texto = texto
        self.caractere = caractere