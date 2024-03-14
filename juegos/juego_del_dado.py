from random import randint
def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    puntuacion_usuario = 0
    puntuacion_computador = 0
    while puntuacion_usuario < 30 or puntuacion_computador < 30:
        print("Aprieta ENTER para lanzar un dado")
        x = input()
        puntaje1 = randint(1,6)
        puntuacion_usuario = puntuacion_usuario + puntaje1
        print("Sumaste" + " " + str(puntaje1) + " " + "puntos")
        print("Tienes" + " " + str(puntuacion_usuario) + " " + "puntos")
        if puntuacion_usuario >= 30:
            print("GANASTE!!!!!!!!!!")
            break
        puntaje2 = randint(1,6)
        puntuacion_computador = puntuacion_computador + puntaje2
        print("CPU sumó" + " " + str(puntaje2) + " " + "puntos")
        print("CPU tiene" + " " + str(puntuacion_computador) + " " + "puntos")
        if puntuacion_computador >= 30:
            print("La CPU ha ganado")
            break
