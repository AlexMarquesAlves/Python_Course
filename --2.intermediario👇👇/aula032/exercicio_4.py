print("-" * 12, "Exercício_4", "-" * 12)
"""
4 - Fizz Buzz - Se o parameter da função for divisível por 3, retorne
fizz, se o parameter da função for divisível por 5, retorne buzz. Se o
parameter da função for divisível por 5 e por 3, retorne FizzBuzz, caso
contrário retorne o número enviado
"""
print()


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} é divisível por 3 e 5'
    elif n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    elif n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    else:
        return n


print(fb(6))
print(fb(10))
print(fb(15))

print()
print("-" * 8, "Resultado no curso", "-" * 8)
print()


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'

    return n


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
