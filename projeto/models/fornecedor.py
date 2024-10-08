from projeto.models.endereco import Endereco
from projeto.models.juridica import juridica

class Fornecedor(juridica):

    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.produto = produto

    def __str__(self) -> str:
        return(
               f"{super().__str__()}" 
               f"\nID: {self.id}"  
               f"\nNome: {self.nome}"  
               f"\nTelefone: {self.telefone}"  
               f"\nEmail: {self.email}"  
               f"\nEndereço: {self.endereco}"  
               f"\nCNPJ: {self.cnpj}"  
               f"\nInscrição Estadual: {self.inscricaoEstadual}"  
               f"\nProduto: {self.produto}")