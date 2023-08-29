#ESTRUCTURAS CONDICIONALES
#EJERCICIO 1
x = 10
def sorteo():
    opcion = int(input("\nIngrese un número del 1 al 15 para ganar el sorteo"))
    if opcion > x or opcion < x:
        print("\nOpción incorrecta, ingrese nuevamente...")

    else:
        opcion == x
        print("Usted ha ganado el sorteo!")


#EJERCICIO 2
x = 10
def sorteo():
    opcion = int(input("\nIngrese un número del 1 al 15 para ganar el sorteo"))
    if opcion > x:
        print("\nFalto un poco, seguí participando...")

    elif opcion < x:
        print("\nTe pasaste, a seguir intentando...")

    else:
        opcion == x
        print("Usted ha ganado el sorteo!")


#EJERCICIO 3
lunes = "Es el primer día de la semana"
martes = "El martes, es el segundodía de la semana"
miercoles = "Usted a ingresado el día miércoles"
jueves = "Ya falta poco para finalizar la semana laboral"
viernes = "Sí señor! ya es viernes"
sabado = "Ya estamos en fin de semana"
domingo = "Vamos, que ya se acaba el finde..."
def dias():
    opcion = input("\nIngrese un día de la semana para recibir un mensaje")
    if opcion == lunes:
        print(lunes)
    elif opcion == martes:
        print(martes)
    elif opcion == miercoles:
        print(miercoles)
    elif opcion == jueves:
        print(jueves)
    elif opcion == viernes:
        print(viernes)
    elif opcion == sabado:
        print(sabado)
    elif opcion == domingo:
        print(domingo)
    else:
        print("El valor ingresado no corresponde a lo solicitado!")


#EJERCICIO 4
x = "es vocal"
a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
def vocal():
    opcion = input("\nIngrese una letra del abecedario")
    if opcion == a:
        print(x)
    elif opcion == e:
        print(x)
    elif opcion == i:
        print(x)
    elif opcion == o:
        print(x)
    elif opcion == u:
        print(x)
    else:
        print("Usted a ingresado una consonante!")


#ESTRUCTURAS REPETITIVAS
#EJERCICIO 1
x = -1
def calculadora():
    resultado = n1 + n2
    print("Se le solicitará ingresar 2 números entre -5 y 10.")
    print("Se realizará la suma pertinente hasta que ingrese un valor que genere un error!\n")
    n1 = int(input("\nIngrese un número del -5 al 10"))
    n2 = int(input("\nIngrese un número del -5 al 10"))

    for resultado in n1:
        if n1 == x:
            print("Ha ingresado un valor que produjo una falla en el sistema!")

    for resultado in n2:
        if n2 == x:
            print("Ha ingresado un valor que produjo una falla en el sistema!")
    else:
        return resultado
    
#EJERCICIO 2
