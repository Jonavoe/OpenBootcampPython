def archivo(fichero, datos):
    f = open(fichero, 'w')
    
    
    f.write(lista)
    
    f.close()


lista = 'Donec ac fringilla lectus, non lacinia massa. Integer ut nisl ut mauris molestie fermentum quis eget odio. Vestibulum ultricies orci vitae dui euismod facilisis. Nunc vitae erat semper, luctus tortor sollicitudin, viverra sem. Suspendisse malesuada justo eu volutpat accumsan. Pellentesque eget rutrum ex. Fusce varius tellus in quam suscipit, eget aliquam mauris viverra. In ac venenatis odio. Quisque rhoncus pellentesque scelerisque. In hac habitasse platea dictumst.\n'

archivo('archivo.txt', lista)
