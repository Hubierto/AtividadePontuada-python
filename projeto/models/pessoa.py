from abc import ABC
from .endereco import Endereco

class Pessoa(ABC):

    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco

    def _verificar_id(self, valor: int) -> int:
        self._verificar_id_tipo_invalido(valor)
        self._verificar_id_negativo(valor)
        return valor

    def _verificar_nome(self, valor: str) -> str:
        self._verificar_nome_tipo_invalido(valor)
        self._verificar_nome_vazio(valor)
        return valor

    def _verificar_telefone(self, valor: str) -> str:
        self._verificar_telefone_tipo_invalido(valor)
        return valor

    def _verificar_email(self, valor: str) -> str:
        self._verificar_email_tipo_invalido(valor)
        return valor

    def _verificar_id_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("ID inválido!")

    def _verificar_id_negativo(self, valor):
        if valor <= 0:
            raise ValueError("ID deve ser positivo!")

    def _verificar_nome_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("Nome inválido!")

    def _verificar_nome_vazio(self, valor):
        if not valor.strip():
            raise ValueError("Nome não pode ser vazio!")

    def _verificar_telefone_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("Telefone inválido!")

    def _verificar_email_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("Email inválido!")
