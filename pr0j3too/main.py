import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pr0j3too.models.juridica import Juridica
from pr0j3too.models.fornecedor import Fornecedor
from pr0j3too.models.endereco import Endereco
from pr0j3too.models.enums.unidadefederativa import UnidadeFederativa

os.system("cls || clear")

fornecedor1 = Fornecedor(111, "Miguel", "71923232323", "M@gmail.com", Endereco("Praça das núvens", "001", "L", "0121213", "Sei lá", UnidadeFederativa.RIO_DE_JANEIRO), "983815634", "0828495", "Abacate" )
juridica1 = Juridica(123, "Manuel", "71988776655", "M@gmail.com", Endereco("Praça do sol", "14", "E", "892374", "Salvador", UnidadeFederativa.BAHIA), "82375478657832", "81358579-815") 

print(fornecedor1)
print(juridica1)