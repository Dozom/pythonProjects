import threading
# FILS 3
#en definir una funció de fil, els arguments s'han de pasar d'aquesta manera
def contar(*args):
   contador=args[0]
   incremento= args[1]
   limite=args[2]
   num_hilo=args[3]
   while contador<=limite:               
       print('hilo:', num_hilo, 'contador:', contador)
       contador+=incremento

for num_hilo in range(3):
   #les funcions de fil han de rebre els arguments amb *args
   hilo = threading.Thread( target=contar, args=( 0,1,10, num_hilo,))   
   hilo.start()
