import threading
import time

totalNumerosPrimers = 0 

def buscaNombresPrimers(numeroInici, numeroFinal):
    global totalNumerosPrimers
    for i in range(numeroInici, numeroFinal):
        if (esPrimer(i)):
            totalNumerosPrimers += 1
            print(i)

def esPrimer(num):
    if num < 2:
        return False
    for j in range(2, num):
        if (num % j == 0):
            return False
    return True

final = int(input("Introdueix el numero final:"))
start = time.time()
buscaNombresPrimers(1,final)
end = time.time()
print("Sense fils: ",end - start," total numeros primers: ",totalNumerosPrimers)
