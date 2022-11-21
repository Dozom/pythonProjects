import Crypto
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def writeFile(file, content):
    with open(file,"w") as f:
        f.write(content)

def readFile(file):
    with open(file,"r") as f:
        return f.read()

def generateKeyPair():
    random_generator = Crypto.Random.new().read
    private_key = RSA.generate(1024, random_generator)
    public_key = private_key.publickey().export_key().decode()
    private_key = private_key.export_key().decode()
    return public_key, private_key

def cipher(public_key, text):
    cipher = PKCS1_OAEP.new(key=public_key)
    return cipher.encrypt(text)

def uncipher(private_key, cipheredtext):
    cipher = PKCS1_OAEP.new(key=private_key)
    return cipher.decrypt(cipheredtext)

def keysFromFiles():
    puk = RSA.import_key(readFile("public_key.pem"))
    prk = RSA.import_key(readFile("private_key.pem"))

def demoTest():
    text = b'hola'
    #generate Keys
    public_key, private_key = generateKeyPair()
    #write Keys into files
    writeFile("public_key.pem",public_key)
    writeFile("private_key.pem",private_key)
    #cipheredText
    textXifrat = cipher(puk, text)
    print("El text xifrat és: ", textXifrat)
    #uncipheredText
    textDesxifrat = uncipher(prk, textXifrat)
    print("El text desxifrat és: ",textDesxifrat.decode())

if __name__ == '__main__':
    while True:
        try:
            option = int(input("""Introdueix una de les següents opcions per tal de fer servir el programa:
                    0. Demo del programa. (Official working)
                    1. Generar i escriure les claus a fitxers.
                    2. Llegir les claus desde fitxers.
                    3. Xifrar.
                    4. Desxifrar.
                  """))
            if option == 0:
                demoTest()
            if option == 1:
                #generate Keys
                public_key, private_key = generateKeyPair()
                #write Keys into files
                writeFile("public_key.pem",public_key)
                writeFile("private_key.pem",private_key)
            if option == 2:
                keysFromFiles()
            if option == 3:
                #cipheredText
                textXifrat = cipher(puk, text)
                print("El text xifrat és: ", textXifrat)
            if option == 4:
                #uncipheredText
                textDesxifrat = uncipher(prk, textXifrat)
                print("El text desxifrat és: ",textDesxifrat.decode())
        except:
            print("Hi ha hagut un error.")
            break


