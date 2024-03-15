import random
def memoria():
    k=""
    for i in range(random.randint(3,8)):
        n=random.randint(1,9)
        print(n)
        k+=str(n)
    a=input("agrega todos los numeros que viste sin espacio")
    numero=str(a)
    if numero == k:
      print("Ganaste! :)")
    else:
      print(f"Perdiste, la secuencia es {k}")

memoria()
