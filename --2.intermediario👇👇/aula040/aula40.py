# add , update, clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
print(f'----Exemplos----')
s1 = {1,2,3,4,5}

for v in s1:
  print(v)

print(f'----Exemplo add----')

s2 = set()
s2.add(1)
s2.add(2)
s2.add((1,2,3,'Luiz'))
print(s2)

print(f'----Exemplo discard----')

s3 = set()
s3.add(1)
s3.add(2)
s3.discard(2)
print(s3)

print(f'----Exemplo update----')

s4 = set()
s4.update('Python')
print(s4)

s5 = set()
s5.update([1, 2, 3, 4, 5], {5, 6, 7, 8})
print(s5)

print()

l1 = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 'Luiz', 'Luiz']
l1 = set(l1)
l1 = list(l1)
print(l1)
print(l1[-1])

print(f'----Exemplo Union, | ----')

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2

print(s3)

print(f'----Exemplo intersection----')

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 & s2

print(s3)

print(f'----Exemplo difference----')

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 - s2
s4 = s2 - s1

print(s3)
print(s4)

print(f'----Exemplo symmetric_difference----')

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 ^ s2

print(s3)
print()
print(f'----Exemplo nas listas----')
l1 = ['Luiz','João','Maria',]
l2 = ['João','Maria','Maria', 'Luiz','Luiz','Luiz','Luiz','Luiz','Luiz','Luiz',]
l1 = list(set(l1))
l2 = list(set(l2))

print(l1, l2)

print()
l1 = ['Luiz','João','Maria',]
l2 = ['João','Maria','Maria', 'Luiz','Luiz','Luiz','Luiz','Luiz','Luiz','Luiz',]

if set(l1) == set(l2):
  print(f'L1 é igual a L2')
else:
  print(f'L1 é diferente de L2')
