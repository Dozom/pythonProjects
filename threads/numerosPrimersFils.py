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
# fil 1: de 1 a la meitat del nombre
# fil 2: de la meitat fins al final
fil1 = threading.Thread(target=buscaNombresPrimers, args=(1,final//2))
fil2 = threading.Thread(target=buscaNombresPrimers, args=(final//2, final))
fil1.start()
fil2.start()
fil1.join()
fil2.join()
end = time.time()
print("Amb fils: ",end - start," total de numeros primers: ",totalNumerosPrimers)
