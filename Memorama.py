import random

# Variables globales
J1 = J2 = ""
PUNTAJE_J1 = PUNTAJE_J2 = 0
TURNO = True

# Divide la lista en 'n' partes
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

# Crea las 2 lista de números random
def crear_lista_random():
    lista = []
    for i in range(2):
        lista_temporal = ""
        for j in range (1, 19):
            lista_temporal = j
            lista.append(lista_temporal)
    random.shuffle(lista)
    return lista

# Dibuja la matriz (cuadrada)
def crear_matriz(matriz):
    for i in range(len(matriz)):
        fila = ""
        for j in range(len(matriz)):
            if matriz[i][j] == "**":
                fila += str(matriz[i][j]) + " "
            elif matriz[i][j] <= 9:
                fila += ("0" + str(matriz[i][j]) + " ")
            else:
                fila += str(matriz[i][j]) + " "    
        print(fila)

# Enmascarar matriz
def enmascarar_lista(lista):
    for i in range(len(lista)):
        for j in range (len(lista)):
            lista[i][j] = "**"
    return lista

# Desenmascara una lista
def desenmascarar(lista_matriz, lista_mascara, x1, y1, x2, y2):
    global TURNO
    
    if x1 <= 0 or x1 > 6 or y1 <= 0 or y1 > 6 or x2 <= 0 or x2 > 6 or y2 <= 0 or y2 > 6:
        print("Tiene un número fuera del rango; el mínimo es 1 y el máximo es 6")
        print("Perdiste tu turno, por no prestar atención")
        TURNO = not TURNO 
    elif x1 == x2 and y1 == y2:
        print("No se pueden repetir las casillas durante la misma jugadas")
        print("Perdiste tu turno, por no prestar atención")
        TURNO = not TURNO
    elif lista_mascara[x1 - 1][y1 - 1] != "**" or  lista_mascara[x2 - 1][y2 - 1] != "**":
        print("No se pueden obtener las casillas que ya han sido desbloqueadas")
        print("Perdiste tu turno, por no prestar atención")
        TURNO = not TURNO
    elif lista_matriz[x1 - 1][y1 - 1] == lista_matriz[x2 - 1][y2 - 1]:
        lista_mascara[x1 - 1][y1 - 1] = lista_matriz[x1 - 1][y1 - 1]
        lista_mascara[x2 - 1][y2 - 1] = lista_matriz[x2 - 1][y2 - 1]
        print("Primer número elegido: " + str(lista_matriz[x1 - 1][y1 - 1]))
        print("Segundo número elegido: " + str(lista_matriz[x2 - 1][y2 - 1]))
        agregar_puntaje()
    else:
        print("Fallaste")
        TURNO = not TURNO

# X1, Y1, X2, Y2 de la matriz
def coordenadas():
    coords = []
    
    while True:
        X1 = input("Introduzca el primer número de la fila: ")
        Y1 = input("Introduzca el primer número de la columna: ")
        X2 = input("Introduzca el segundo número de la fila: ") 
        Y2 = input("Introduzca el segundo número de la columna: ")
        
        if X1.isnumeric() == False or Y1.isnumeric() == False or X2.isnumeric() == False or Y2.isnumeric() == False:
            print("Alguna de las coordenadas tiene valores alfanuméricos, verifique")
        else:
            break
 
    coords.append(int(X1))
    coords.append(int(Y1))
    coords.append(int(X2))
    coords.append(int(Y2))
    return coords

# Sumar puntaje a los jugadores
def agregar_puntaje():
    global TURNO, PUNTAJE_J1, PUNTAJE_J2
    if TURNO:
        PUNTAJE_J1 += 1
    else:
        PUNTAJE_J2 += 1

# Puntaje de los jugadores
def puntaje_general():
    global J1, J2
    global PUNTAJE_J1, PUNTAJE_J2
    print("El puntaje de " + J1 + " es " + str(PUNTAJE_J1))
    print("El puntaje de " + J2 + " es " + str(PUNTAJE_J2))

# Continuar juego
def continuar():
    while True:
        k = input("¿Quieren seguir jugando? \n")
        if k.isnumeric():
            print("La respuesta tiene valores alfanuméricos, verifique")
        else:     
            if k == "Si" or k == "Sí" or k == "SI" or k == "SÍ" or k == "si":
                return
            elif k == "No" or k == "NO" or k == "no":
                puntaje_general()
                exit()
            
# Fin del juego
def fin_del_juego():
    global J1, J2
    global PUNTAJE_J1, PUNTAJE_J2
    global lista_mascara, lista_matriz
    
    if lista_mascara == lista_matriz:
        if PUNTAJE_J1 == PUNTAJE_J2:
            print("EMPATE")
        elif PUNTAJE_J1 > PUNTAJE_J2:
            print(J1 + " es el ganador con " + str(PUNTAJE_J1))
        else:
            print(J2 + " es el ganador con " + str(PUNTAJE_J2))

# Creamos la lista de números random y los copiamos a dos listas nuevas
lista_random = crear_lista_random()
lista_matriz = lista_random.copy()
lista_mascara = lista_random.copy()

# Hacemos un split a la lista para tener una lista de listas, es decir, nuestra matriz
lista_mascara = list(chunks(lista_mascara, 6))
lista_matriz = list(chunks(lista_matriz, 6))

# Enmascaramos nuestra lista
enmascarar_lista(lista_mascara)

# GAME
print("¡BIENVENIDO AL JUEGO DEL MEMORAMA! \n" )
J1 += input("Introduzca el nombre del primer jugador: ")
J2 += input("Introduzca el nombre del segundo jugador: ")

while True:
    puntaje_general() # Puntaje de los dos jugadores
    crear_matriz(lista_mascara) # Dibuja el tablero
    
    if TURNO: print("El turno es de: " + J1) # Sistema de turnos
    else: print("El turno es de: " + J2)
    
    temp = coordenadas() # Obtiene las coordenadas temporalmente por ronda
    X1 = temp[0]
    Y1 = temp[1]
    X2 = temp[2]
    Y2 = temp[3]
    desenmascarar(lista_matriz, lista_mascara, X1, Y1, X2, Y2) # Sistema de desenmascaramiento
    
    fin_del_juego() # Comprueba si el juego ya acabó
    continuar() # Pregunta al usuario si desea seguir jugando