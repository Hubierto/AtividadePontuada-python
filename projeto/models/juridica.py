from abc import ABC
from models.endereco import Endereco
from models.pessoa import Pessoa

class juridica(Pessoa, ABC):

    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual

    def __str__(self) -> str:
        return( 
              f"{super().__str__()}"
              f"\nCnpj: {self.cnpj}"
              f"\nInscrição Estadual: {self.inscricaoEstadual}"
              ) 