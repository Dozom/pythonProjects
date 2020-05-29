#coding=utf-8
"""
        __        __                                  ______
	|  |      |  |                                |   _  \
 	|  |  __  |  |  ________   ______   ________  |  | \  \
	|  | /  \ |  | |   __   | |___   | |   __   | |  |  \  \
 	|  |/    \|  | |  |  |  |    /   / |  |  |  | |  |   \  \  
        |            | |  |  |  |   /   /  |  |  |  | |  |   /  /
        |     /\     | |  |  |  |  /   /   |  |  |  | |  |  /  /
 	|    /  \    | |  |__|  | /   /_   |  |__|  | |  |_/  /
 	|___/    \___| |________||______|  |________| |______/

	- If you want to see how it works, read the README from github
	  Thank's ;D
"""
user = raw_input("Escribe el usuario del que quieres encontrar la contraseña: ")
x = os.popen("cat /etc/shadow | grep {0}".format(user)).read()
print(x)
x = x.split("$")
y = x[3].split(":")
y = y[0].replace("\n","")
f = open("xd.dic")
linea = f.readline()
def leer(x,salt,hashy):
	global linea
	while(linea != ""):
		linea = f.readline()
		linea = linea.replace("\n","")
		hashcrack = os.popen("mkpasswd -m {0} {1} {2}".format(x,linea,salt)).read()
		hashcrack = hashcrack.split("$")
		hashcrack = str(hashcrack[3].replace(" ",""))
		hashcrack = str(hashcrack.replace("\n",""))
		hashy = str(hashy.replace(" ",""))
		hashy = str(hashy.replace("\n",""))
		if(hashy == hashcrack):
			print("Tu contraseña es: {0}".format(linea))
		if(linea == ""):
			break
if(x[1] == "1"):
	salt = x[2]
	c = "md5"
	leer(c,salt,y)
elif(x[1] == "2a"):
	salt = x[2]
	c = "2a"
	leer(c,salt,y)
elif(x[1] == "5"):
	salt = x[2]
	c = "SHA-256"
	leer(c,salt,y)
elif(x[1] == "6"):
	salt = x[2]
	c = "SHA-512"
	leer(c,salt,y)
