print("-"*12, "Exercício_3", "-"*12)
"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um 
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
print()


def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual / 100))


aumento_percentual(50, 10)
aumento_percentual(100, 10)
aumento_percentual(10, 10)
aumento_percentual(15, 100)
