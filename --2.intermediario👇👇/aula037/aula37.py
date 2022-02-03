print('-'*10, 'Tuplas em Python', '-'*10)
print('-'*10, 'Exemplo_1', '-'*10)

t1 = 1, 2, 'Luiz', 4, 5
t2 = 6, 7, 8, 9, 10
t3 = t1 + t2

n1, n2, n3, *_, n10 = t3

print(n3)
print(n10)

print('-'*10, 'Exemplo_2', '-'*10)

t1 = (1, 2, 'Luiz', 4, 5)*20
print(t1)

print('-'*10, 'Exemplo_3', '-'*10)

t_1 = (1, 2, 3, 4, 5)
t_1 = list(t_1)
t_1[1] = 3000
t_1 = tuple(t_1)

print(t_1)
