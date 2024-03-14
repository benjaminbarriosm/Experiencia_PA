def adivinar_par_o_impar():
    print("Voy a elegir un numero y tienes que adivinar si es PAR o IMPAR")
    nn=input()
    import random
    numero=random.randint(0,100)
    if numero%2==0:
        par=True
    else:
        par=False
    if nn=="PAR":
        npar=True
    else:
        npar=False
    if par==True and npar==True:
        print("Ganaste!")
        print("Yo elegí el ",numero)
    elif par==False and npar==False:
        print("Ganaste!")
        print("Yo elegí el ",numero)
    elif par==True and npar==False:
        print("Perdiste :(")
        print("Yo elegí el ",numero)
    else:
        print("Perdiste :(")
        print("Yo elegí el ",numero)
