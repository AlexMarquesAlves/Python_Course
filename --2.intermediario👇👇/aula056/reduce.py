from dados import produtos, pessoas, lista
from functools import reduce
print('----> Exemplo de Acumulador')
acumula = 0
for item in lista:
    acumula += item

print(acumula)

