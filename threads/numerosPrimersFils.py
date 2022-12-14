import threading
import time

totalNumerosPrimers = [] 

def buscaNombresPrimers(numeroInici, numeroFinal):
    global totalNumerosPrimers
    for i in range(numeroInici, numeroFinal):
        if (esPrimer(i)):
            totalNumerosPrimers.append(i)
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
fil1 = threading.Thread(target=buscaNombresPrimers, args=(1,final))
fil2 = threading.Thread(target=buscaNombresPrimers, args=(1, final))
fil1.start()
fil2.start()
fil1.join()
fil2.join()
end = time.time()
print("Amb fils: ",end - start)


            
