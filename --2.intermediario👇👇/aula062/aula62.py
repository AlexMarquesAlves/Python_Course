
from vendas.calc_precos import aumento, reducao
from vendas.formata import preco as formata

price = 49.90
price_com_aumento = aumento(valor=price, porcentagem=15, formata=True)
print(price_com_aumento)

price_com_reducao = reducao(valor=price, porcentagem=15, formata=True)
print(price_com_reducao)

print(formata.real(50.95))
