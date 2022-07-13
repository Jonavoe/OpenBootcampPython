import time
hora = int(time.strftime('%H'))
minutos = int(time.strftime('%M'))
segundos = int(time.strftime('%S'))

print() 
print('La Hora Es',hora,minutos,segundos)
print()   
horaV = 19 - hora
minutosV = 60 - minutos
segundosV =  60 - segundos

# print('Falta para volver a casa',horaV,'Horas',minutosV,'Minutos',segundosV,'Segundos')

if hora <= 19:
    print('Todavia no es hora de volver a casa, Faltan:',horaV,'Horas',minutosV,'Minutos',segundosV,'Segundos')
else:
    print('Es hora de volver a casa')

print()
print('Funcion Volver A Casa')
#Funcion volver a casa
def horaDeVolver(horaV, minutosV, segundosV): #Ejeplo horaDeVolver(19,60,60) 
    h = hora
    m = minutos
    s = segundos
    horaVolver = horaV -h
    minutosVolver =  minutosV - m
    segundosVolver = segundosV - s
    
    print('Falta para volver a casa',horaVolver,'Horas',minutosVolver,'Minutos',segundosVolver,'Segundos')

horaDeVolver(19,60,60)