import random
def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    x=""
    usuario=input("elige entre ")
    opcion=["piedra","papel","tijera"]
    aleatorio=random.choice(opcion)
    if usuario==aleatorio:
        x="empate"
    elif usuario=="piedra" and aleatorio=="papel":
        x="perdiste"
    elif usuario=="piedra" and aleatorio=="tijera":
        x="ganaste"
    elif usuario=="papel" and aleatorio=="piedra":
        x="ganaste"
    elif usuario=="papel" and aleatorio=="tijera":
        x="perdiste"
    elif usuario=="tijera" and aleatorio=="piedra":
        x="perdiste"
    elif usuario=="tijera" and aleatorio=="papel":
        x="ganaste"
    print(x)
    pass