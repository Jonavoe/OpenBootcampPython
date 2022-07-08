import math

print('----------------------')
print('Indice de Masa Coporal')
print('----------------------')

peso = int(input('Ingrese su peso en kg: '))
estatura = float(input('Ingrese su estatura en metros: '))

imc = round(peso / (estatura ** 2),2)

print('Tu indicie de masa corporal es', imc)

if(imc <= 18.59): {
    print('peso menor a lo normal')
}
elif(imc >= 18.69 and imc <= 24.99): {
    print('normal')
}
elif(imc >= 25 and imc <= 29.9): {
    print('sobrepeso')
}
else: {
    print('Obesidad')
}
