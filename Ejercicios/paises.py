def main():

    paises = set({})
    def agregarPaises(pais):
        paises.add(pais)
                    
    agregarPaises(input('Agrega un Pais: ').capitalize())
    agregarPaises(input('Agrega un Pais: ').capitalize())
    agregarPaises(input('Agrega un Pais: ').capitalize())
    agregarPaises(input('Agrega un Pais: ').capitalize())
    agregarPaises(input('Agrega un Pais: ').capitalize())

    print(list(paises))

if __name__== "__main__" :
    main()