# Módulos padrão do Python
# Módulos são arquivos .py (que contem código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os módulos padrão do python em:
# https://docs.python.org/3/py-modindex.html
from sys import platform as so  # módulo sys
from random import randint as randint_original, random
import pymysql  # pip install pymysql | pip uninstall pymysql

print(f'\t\tExemplo módulo - sys')
print(so)

print(f'\t\tExemplo módulo - random')


def randint(*args):  # sobrescreve o módulo original...
    return 'hahaha'


for i in range(10):
    print(randint_original(0, 10), random())

print(randint())
