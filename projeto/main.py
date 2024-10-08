import os
import sys

sys.path.append(os.path.abspath('.'))

from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidadefederativa import UnidadeFederativa


os.system("cls || clear")

fornecedor1 = Fornecedor(9009, "Lucaas", "71 9 87876565", "L@gmail.com", Endereco("praça do sol", "097", "I","47856983", "Salvador", UnidadeFederativa.BAHIA), "14268568", "068659", "Chocolate")

print(fornecedor1)