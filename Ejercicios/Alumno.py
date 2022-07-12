class Alumno:
    Nombre = ""
    Nota = 0
    
    def cambiarNombre(self, Nombre):
        self.Nombre = Nombre
        
    def cambiarNota(self, nota):
        self.Nota = nota
        
Harryson = Alumno()

Harryson.cambiarNombre('Harryson')
print(Harryson.Nombre)

Harryson.cambiarNota(6)

if Harryson.Nota >= 6:
    print('El alumno', Harryson.Nombre, 'Aprobo la materia con un', Harryson.Nota)
else:
    print('El alumno', Harryson.Nombre, 'Desaprobo la materia con un', Harryson.Nota)