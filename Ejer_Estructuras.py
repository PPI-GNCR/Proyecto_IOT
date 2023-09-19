#ESTRUCTURAS CONDICIONALES
#EJERCICIO 1
x = 10

opcion = int(input("\nIngrese un número del 1 al 15 para ganar el sorteo"))
if opcion > x or opcion < x:
    print("\nOpción incorrecta, ingrese nuevamente...")

else:
    opcion == x
    print("Usted ha ganado el sorteo!")


#EJERCICIO 2
x = 10

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
print("Se le solicitará ingresar 2 números entre -5 y 10.")
print("Se realizará la suma pertinente hasta que ingrese un valor que genere un error!\n")

while True:
    n1 = int(input("\nIngrese un número del -5 al 10\n"))
    if n1 == -1:
        print("Ha ingresado un valor que produjo una falla en el sistema!")
        break # se sale del bucle al ingresar -1.
    if n1 <-5 or n1 > 10:
        print("Ha ingresado un valor fuera del rango solicitado!")
        continue # se sigue pidiendo números

    n2 = int(input("\nIngrese un número del -5 al 10\n"))
    if n2 == -1:
        print("Ha ingresado un valor que produjo una falla en el sistema!")
        break # se sale del bucle al ingresar -1.
    if n2 <-5 or n1 > 10:
        print("Ha ingresado un valor fuera del rango solicitado!")
        continue # se sigue pidiendo números

    resultado = n1 + n2
    print("El resultado de la suma es: ", resultado)


#EJERCICIO 2
cantidad_numeros = int(input("Ingrese la cantidad de números que se introducirán: \n")) # solicitamos la cantidad de números a introducir

mayor_cero = 0
menor_cero = 0
igual_cero = 0

for i in range(cantidad_numeros):
    numero = float(input("Ingrese un número entre -15 y 15: ")) # solicitamos los números
    
    if numero > 0:
        mayor_cero += 1
    elif numero < 0:
        menor_cero += 1
    elif numero <-15 or numero > 15:
        print("Ha ingresado un valor fuera del rango solicitado!")
    else:
        igual_cero += 1

# mostramos los resultados
print("Números mayores que 0:", mayor_cero)
print("Números menores que 0:", menor_cero)
print("Números iguales a 0:", igual_cero)


#EJERCICIO 3
while True:
    caracter = input("Ingrese un caracter (LETRA del abecedario) para definir si es VOCAL o NO VOCAL!\n O ingrese 0 (cero) para salir del sistema. \n")
    
    if caracter == '0':
        print("Gracias por utilizar el sistema.")
        break  # salimos del bucle y finaliza.

    if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("VOCAL")
    else:
        print("NO VOCAL")


#EJERCICIO 4
suma = 0
contador = 0

while True:
    numero = float(input("Se solicitará que ingrese números hasta que ingrese 0 (cero), para realizar un cálculo. \n"))
    
    if numero == 0:
        if contador == 0:
            print("No se han ingresado números.")
        else:
            media = suma / contador
            print(f"La suma de los números es: {suma}")
            print(f"La media de los números es: {media}")
        break  # se sale del bucle al ingresar 0.
    
    suma += numero
    contador += 1
