from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero
reverso = 10
total = 0
for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

cpf_primeiros_3 = novo_cpf[0:3]
cpf_segundos_3 = novo_cpf[3:6]
cpf_terceiros_3 = novo_cpf[6:9]
cpf_ultimos_digitos = novo_cpf[9::]
# print(novo_cpf)
n1 = cpf_primeiros_3
n2 = cpf_segundos_3
n3 = cpf_terceiros_3
n4 = cpf_ultimos_digitos
cpf_formatado = f'{n1}.{n2}.{n3}-{n4}'
print()
print(cpf_formatado)
