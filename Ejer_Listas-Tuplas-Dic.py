#Ejercicios Listas
listaFlia = ["Roberto", "Noemi", "Alejandro", "Cristian", "Verónica", "Guillermina", "Diego", "Alberto", "Lucrecia", "Andrés", "Nidia"]

listaTempAgosto = [18, 15, 22, 31, 19, 18, 22, 28, 30, 29, 21, 18, 24, 22, 17, 18, 19, 20, 24, 25, 18, 18, 18, 19, 19, 20, 23, 22, 
                   20, 21, 25]

listaCiudades = ["Salta", "San Miguel de Tucumán", "Bariloche", "San Juan", "Mendoza", "San Martín de los Andes", "Villa Mercedes",
                 "Río Cuarto", "La Falda", "Santa Rosa", "Neuquén", "Plottier", "Ushuahia", "Río Gallegos", "El Calafate", 
                 "Comodoro Rivadavia", "Puerto Madryn"]

listaFechas = ['13/10', '15/10', '12/06', '15/08', '01/03', '08/10', "CumpleCris", "CumpleCeci", "CumplePili", "CumpleGasti", 
               "CumpleTito", "CumpleAdri",]

#1
listaFlia.sort()
print(listaFlia)
#2
listaTempAgosto.sort()
print(listaTempAgosto)
#3
listaTempAgosto.extend([26, 20, 20, 21, 23, 20, 26, 27, 26, 27, 27, 26, 28, 27, 31])
print(listaTempAgosto)
#4
listaFlia
print(listaFlia[0:7])
#5
del listaCiudades[15]
print(listaCiudades)
#6
listaTodas = listaFlia + listaTempAgosto + listaCiudades + listaFechas
print(listaTodas)


#Ejercicios Tuplas
tuplaFlia = ("Noemi", "Alejandro", "Cristian", "Verónica", "Guillermina", "Diego", "Alberto")
tuplaCiudades = ("Salta", "Bariloche", "San Juan", "Mendoza", "Neuquén", "Ushuahia", "El Calafate", "Puerto Madryn")
tuplaFechas = ('13/10', '15/10', '12/06', '15/08', '01/03', '08/10')

listaTuplas = [tuplaFlia, tuplaCiudades, tuplaFechas]
print(listaTuplas)


#Ejercicio Diccionario
#1
diccUno = {11846511:'Raúl', 12543942:'Noemi', 27477631:'Alejandro', 29648115:'Cristian'}
diccUno [5258734] = 'Andrés'
diccUno [6987123] = 'Nidia'
diccUno [6001854] = 'Alberto'
diccUno [7555431] = 'Lucrecia'

print(diccUno)

#2
diccDos = {'':[]}
n = 0
def añadir (telefono):
    cantidad = len(diccDos)
    global n
    n+=1
    diccDos[str(n)] = [telefono]

diccDos.pop("")
añadir(155471788)
añadir(156784169)
añadir(154852654)
añadir(155963741)

print(diccDos)

#ESTRUCTURAS CONDICIONALES

#EJERCICIO 1
x = 10
def sorteo():
    opcion = int(input("\nIngrese un número del 1 al 10"))
    if opcion < 1 or opcion > 10:
        print("\nOpción incorrecta, ingrese nuevamente...")

    elif opcion == 10:
        try:
            print("Usted ha ganado el sorteo!")
        except Exception as descripcionError:
            print("Hubo un ERROR al ingresar un número del 1 al 10...", descripcionError)
    else:
        opcion <10
        print("El número ingresado es mayor a 10!")


