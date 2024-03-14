from random import randint
def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    num = randint(1,10)
    if int(input("Adivina el numero entre 1 y 10": )) == num:
        print("Correcto")
    else:
        print(f"MAL, el numero era {num}")
