from functools import reduce

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

impar = filter(lambda n: n % 2 == 1, numero)

resultado = reduce(lambda x, y: x + y, impar)

print(f'El resultado de la suma de los valores impares es: {resultado}')