
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', '20'))
carrinho.append(('Produto 3', 50))

# total = [(x, y) for x, y in carrinho]
# total = [y for x, y in carrinho]
# total = [float(y) for x, y in carrinho]
total = sum([float(y) for x, y in carrinho])
print(carrinho)
print()
print(f'Soma total: R${total}')
