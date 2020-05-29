"""
	                                      __     
	                                     /\ \    
	 __  __  __    ___   ____     ___    \_\ \   
	/\ \/\ \/\ \  / __`\/\_ ,`\  / __`\  /'_` \  
	\ \ \_/ \_/ \/\ \L\ \/_/  /_/\ \L\ \/\ \L\ \ 
	 \ \___x___/'\ \____/ /\____\ \____/\ \___,_\
	  \/__//__/   \/___/  \/____/\/___/  \/__,_ /
	                                             
	                                             
	
	- Esta es la parte del cliente, es decir la que se conecta al servidor.
	- PonÈis la ip del servidor y autom·ticamente le mandar· un shutdown y se le abrir· un bloc de notas.
	- NOTA: De momento no he conseguido que sea 100% efectivo, ya que se ha de cerrar el notepad para que se apague.
	- Si quit·is el notepad del codigo y dej·is el shutdown mostrar· el mensaje bye bye y se apagar· autom·ticamente.
	- Have fun ;D
"""
import socket
mi_socket = socket.socket()
# en la ip, met√©is la ip del servidor que hab√©is de apagar
mi_socket.connect(('192.168.0.4',23003))
respuesta = mi_socket.recv(1024).decode()
print(respuesta)
mi_socket.close()

