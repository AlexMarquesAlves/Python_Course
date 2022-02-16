
from vendas.calc_precos import aumento, reducao

price = 49.90
price_com_aumento = aumento(valor=price, porcentagem=15)
print(price_com_aumento)

price_com_reducao = reducao(valor=price, porcentagem=15)
print(price_com_reducao)
