from abc import ABC
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa

class Juridica(Pessoa, ABC):

    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_cnpj(cnpj)
        self.inscricaoEstadual = self._verificar_inscricaoEstadual(inscricaoEstadual)

    def _verificar_cnpj(self, valor):
        self._verificar_cnpj_tipo_invalido(valor)
        self._verificar_cnpj_negativo(valor)
        self._verificar_cnpj_vazio(valor)

    def _verificar_inscricaoEstadual(self, valor):
        self._verificar_inscricaoEstadual_tipo_invalido(valor)    
        self._verificar_inscricaoEstadual_vazio(valor)    

    def _verificar_cnpj_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("CNPJ inválido!")

    def _verificar_cnpj_negativo(self, valor):
        if valor <= 0:
            raise ValueError("CNPJ deve ser positivo!")

    def _verificar_cnpj_vazio(self, valor):
        if not valor.strip():
            raise TypeError("CNPJ não pode ser vazio!")

    def _verificar_inscricaoEstadual_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("Inscrição Estadual inválido!")

    def _verificar_inscricaoEstadual_vazio(self, valor):
        if not valor.strip():
            raise TypeError("Incrição Estadual não pode ser vazio!")

    def __str__(self) -> str:
        return( 
              f"{super().__str__()}"
              f"\nCnpj: {self.cnpj}"
              f"\nInscrição Estadual: {self.inscricaoEstadual}"
              ) 