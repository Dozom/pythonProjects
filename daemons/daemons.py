import threading
import time
import logging
 
logging.basicConfig(level=logging.DEBUG,
                   format='(%(threadName)-9s) %(message)s',)
 
def n():
   #non daemon
   logging.debug('Starting')
   contador=0
   while contador<=10:              
      logging.debug(contador)
      contador+=1
   logging.debug('Exiting')
 
def d():
   #dimoni sí
   logging.debug('Starting')
   contador=0
   while contador<=100:              
      logging.debug(contador)
      contador+=1
   logging.debug('Exiting')
 
if __name__ == '__main__':
 
   t = threading.Thread(name='non-daemon', target=n)
   d = threading.Thread(name='daemon', target=d, daemon=True)
 
   d.start()
   t.start()
