class jugador:
    def __init__(self, nombre ,movimiento):
        self.nombre = nombre
        self.movimiento = movimiento

    #Método por el cual le preguntas a la persona a que dirección quiere moverse
    def moverse(self, nombre, dirección):
        print("Introduce la dirección en la que te quieres mover: ")
        dirección = input()
        
 
 '''IDEAS PRINCIPALES EN ESTE APARTADO'''
    
 '''la idea principal para pedirle que donde se quería mover y que cuando pasase por encima de un objeto lo recogiese.'''
 '''y cuando lo tuviese lo llevase a la mochila a soltarlo, y al hacer eso se eliminaria la posicion del objeto'''
 '''y seria un bucle '''
 '''tenia pensado definir tambien las posiciones originales de los objetos y dejarlo indicado para que se tuviese en cuenta cuando se hiciese el apartado de 
  movimiento del jugador'''
