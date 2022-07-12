class Vehiculo:
    Color = "Gris"
    Ruedas = 4
    Puertas = 5
    
class Coche(Vehiculo):
    Velocidad = '300 k/h'
    Cilindrada = '4.6cc'

audi = Coche()
print('La cilindrada del motor es de:', audi.Cilindrada)
print('La velocidad del auto es de:', audi.Velocidad)
print('El color del auto es:', audi.Color)
print('El auto tiene',audi.Ruedas, 'ruedas')
print('El auto tiene',audi.Puertas, 'puertas')

    
