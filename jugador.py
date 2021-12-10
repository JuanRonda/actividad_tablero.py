class jugador:
    def __init__(self, nombre ,movimiento):
        self.nombre = nombre
        self.movimiento = movimiento

    #Método por el cual le preguntas a la persona a que dirección quiere moverse
    def moverse(self, nombre, dirección):
        print("Introduce la dirección en la que te quieres mover: ")
        dirección = input()
        
        
 #la idea principal era pedirle que donde se quería mover y que cuando pasase por encima de un objeto lo recogiese.
 #y cuando lo tuviese lo llevase a la mochila a soltarlo, y al hacer eso se eliminaria la posicion del objeto
 #y seria un bucle 
