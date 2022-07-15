import pickle

from setuptools import sic


class Vehiculo:
    color = ''
    ruedas = 0
    tipo = ''
    puertas = 0
    motor = 0.0
    
    def __init__(self, color, ruedas, tipo, puertas, motor):
        self.color = color
        self.ruedas = ruedas
        self.tipo = tipo
        self.puertas = puertas
        self.motor = motor

#Con este codigo se crea el archivo vehiculo. bin

# scirocco = Vehiculo('Gris', 4, 'Nafta', 5, 3.2)
# f= open('vehiculo.bin', 'wb')
# pickle.dump(scirocco, f)
# f.close()

#Con este codigo se lee el archivo vehiculo.bin
f = open('vehiculo.bin', 'rb')
scirocco = pickle.load(f)
f.close()


print(f'El color es {scirocco.color}\nEl vehiculo tiene {scirocco.ruedas} Ruedas\nEL combustible es {scirocco.tipo}\nEl vehiculo tiene {scirocco.puertas} Puertas\nLa cilindrada del motor es {scirocco.motor}')