import random

# tablero
posiciones = []
tableroJugador = []
def tablero():
    global posiciones,tableroJugador
    fila = []
    for f in range(10):
        for c in range(10):
            fila.append("*")
        posiciones.append(fila)
        fila = []

    for f in range(10):
        for c in range(10):
            fila.append("*")
        tableroJugador.append(fila)
        fila = []

# esta funcion pinta el tablero, un * es una celda vacia
def pintarTablero():
    fila = ""
    for f in range(10):
        for c in range(10):
            if c == 0:
                fila = "*"
            else:
                fila += " *"
        print(fila)
        fila = ""

# esta funcion genera el barco
def generarBarco(longitudBarco,direccion):
    if(direccion == "H"):
        filarandom = random.randint(0, 9)
        columnarandom = random.randint(0, 9) - longitudBarco
        while(columnarandom < 0):
            columnarandom = random.randint(0, 10) - longitudBarco
        hayBarco = checkBarco(filarandom,columnarandom,longitudBarco,direccion)
        if(not hayBarco):
            generarBarcoHorizontal(filarandom,columnarandom,longitudBarco)
        else:
            generarBarco(longitudBarco,direccion)
    if (direccion == "V"):
        filarandom = random.randint(0, 9) - longitudBarco
        columnarandom = random.randint(0, 9)
        while(filarandom < 0):
            filarandom = random.randint(0, 10) - longitudBarco
        hayBarco = checkBarco(filarandom,columnarandom,longitudBarco,direccion)
        if(not hayBarco):
            generarBarcoVertical(filarandom,columnarandom,longitudBarco)
        else:
            generarBarco(longitudBarco,direccion)

def generarBarcoHorizontal(fila,columna,longitudBarco):
    global posiciones
    for i in range(longitudBarco):
        posiciones[fila][columna+i] = "H"



def generarBarcoVertical(fila, columna,longitudBarco):
    global posiciones
    for i in range(longitudBarco):
        posiciones[fila+i][columna] = "V"

def checkBarco(fila,columna,longitudBarco,direccion):
    res = True
    if direccion == "H":
        for i in range(longitudBarco):
            if(posiciones[fila][columna+i] == "H" or posiciones[fila][columna+i] == "V"):
                return res
        res = False
        return res
    elif direccion == "V":
        for i in range(longitudBarco):
            if (posiciones[fila+i][columna] == "H" or posiciones[fila+i][columna] == "V"):
                return res
        res = False
        return res

def imprimirTableroConBarcos():
    global posiciones
    fila = ""
    for f in range(len(posiciones[0])):
        for c in range(len(posiciones)):
            fila += "{0} ".format(posiciones[f][c])
        print(fila)
        fila = ""

def imprimirTableroJugador():
    global tableroJugador
    fila = ""
    for f in range(len(tableroJugador[0])):
        for c in range(len(tableroJugador)):
            fila += "{0} ".format(tableroJugador[f][c])
        print(fila)
        fila = ""


def barcoTocado(filaJugador,columnaJugador):
    global posiciones
    if(posiciones[filaJugador][columnaJugador] == "H" or posiciones[filaJugador][columnaJugador] == "V"):
        return [True,posiciones[filaJugador][columnaJugador]]
    else:
        return [False,"*"]

tablero()
generarBarco(4,"H")
generarBarco(3,"V")
generarBarco(3,"H")
generarBarco(2,"V")
generarBarco(2,"V")
generarBarco(2,"H")
generarBarco(1,"H")
generarBarco(1,"H")
generarBarco(1,"H")
generarBarco(1,"H")
imprimirTableroConBarcos()
aciertos = 0
errores = 0
while(aciertos != 20):
    filaJugador = int(input("Introduce la fila: "))
    columnaJugador = int(input("Introduce la columna: "))

    if(barcoTocado(filaJugador,columnaJugador)[0] == True):
        print("Acertaste!!")
        tableroJugador[filaJugador][columnaJugador] = barcoTocado(filaJugador,columnaJugador)[1]
        imprimirTableroJugador()
        aciertos += 1
        print("aciertos: {0}     errores: {1}".format(aciertos,errores))
    else:
        print("Fallaste manco")
        imprimirTableroJugador()
        errores += 1
        print("aciertos: {0}     errores: {1}".format(aciertos,errores))
print("Se ha terminado el juego, has ganado")