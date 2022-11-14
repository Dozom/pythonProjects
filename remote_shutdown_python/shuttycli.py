import socket
mi_socket = socket.socket()
# en la ip, metéis la ip del servidor que habéis de apagar
mi_socket.connect(('192.168.17.74',23004))
respuesta = mi_socket.recv(1024).decode()
print(respuesta)
mi_socket.close()

