import pytest
from pr0j3too.models.pessoa import Pessoa
from pr0j3too.models.endereco import Endereco

@pytest.fixture
def pessoa_valida():
    pessoa1 = Pessoa(12345, "Rúben", "71988887777", "ruben@gmail.com",Endereco)
    return pessoa1

def test_id_valido(pessoa_valida):
    assert pessoa_valida.id == 12345

def test_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Rúben"

def test_mudar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Roger"
    assert pessoa_valida.nome == "Roger"

def test_numero_valido(pessoa_valida):
    assert pessoa_valida.telefone == "71988887777"

def test_mudar_numero_valido(pessoa_valida):
    pessoa_valida.telefone = "71965656565"
    assert pessoa_valida.telefone == "71965656565"

def test_email_valido(pessoa_valida):
    assert pessoa_valida.email == "ruben@gmail.com"

def test_mudar_email_valido(pessoa_valida):
    pessoa_valida.email = "e@gmail.com"
    assert pessoa_valida.email == "e@gmail.com"

def test_id_negativo():
    with pytest.raises(ValueError, match="ID deve ser positivo!"):
        Pessoa(-12345, "Rúben", "71988887777", "ruben@gmail.com",Endereco)
 
def test_id_tipo_invalido():
    with pytest.raises(TypeError, match="ID inválido!"):
        Pessoa("12345", "Rúben", "71988887777", "ruben@gmail.com",Endereco)
 
def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="Nome inválido!"):
        Pessoa(12345, 000, "71988887777", "ruben@gmail.com",Endereco)
 
def test_nome_vazio():
    with pytest.raises(TypeError, match="Nome não pode ser vazio!"):
        Pessoa(12345, "", "71988887777", "ruben@gmail.com",Endereco)
 
def test_numero_tipo_valido():
    with pytest.raises(TypeError, match="Telefone inválido!"):
        Pessoa(12345, "Rúben", 71988887777, "ruben@gmail.com",Endereco)
 
def test_email_tipo_valido():
    with pytest.raises(TypeError, match="Email inválido!"):
        Pessoa(12345, "Rúben", "71988887777", 123,Endereco)
 