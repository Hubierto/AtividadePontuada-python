import pytest
from projeto.models.juridica import Juridica
from projeto.models.endereco import Endereco

@pytest.fixture
def juridica_valido():
    juridica1 = Juridica(12345, "Rosa", "88998899", "rosa@gmail.com", Endereco, 99999, "001")
    return juridica1

def test_cnpj_valido(juridica_valido):
    assert juridica_valido.cnpj == 12345

def test_nome_valido(juridica_valido):
    assert juridica_valido.nome == "Rosa"

 