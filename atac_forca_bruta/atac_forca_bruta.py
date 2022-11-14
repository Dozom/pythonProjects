from Crypto.Cipher import AES
import hashlib
iv = b"1234567890123456"  #16 bytes valor fix

def generateKeys():
    """ This function generate numbers from 0000 to 9999 and returns it into an array of strings """
    number = "0000"
    numbers = []
    for i in range(0,9999):
        if (len(str(i)) == 1):
            number = "000"+str(i)
        if (len(str(i)) == 2):
            number = "00"+str(i)
        if (len(str(i)) == 3):
            number = "0"+str(i)
        if (len(str(i)) == 4):
            number = str(i)
        numbers.append(number)
    return numbers

# Array of possible passwords
numberKeys = generateKeys()




for key in numberKeys:
    # per cada password
    encoded = key.encode("UTF-8")
    keyhash = hashlib.sha256(encoded)
    
    # xifrar cocacola amb la key
    cipher = AES.new(keyhash.digest(), AES.MODE_CFB, iv)
    encodedtext = cipher.encrypt("coca cola".encode("UTF-8"))
    
    # comprovar si conté el encriptat
    with open("encripted.txt","r") as f:
        if f.read().contains(encodedtext):
            print("la key és: ", key)







keypass="password entrat per teclat"
misllegitdelarxiu ="Extraterrestres de Raticulin sol·liciten els Plànols del Pentàgon per a invasió imminent"

#HASH
key=keypass.encode("UTF-8")  #pasem la variable tipus str a bytes
keyhash = hashlib.sha256(key)


secret = misllegitdelarxiu.encode("UTF-8")  #pasem la variable tipus str a bytes


#XIFRAT
cipher = AES.new(keyhash.digest(), AES.MODE_CFB, iv)
encodedtext = cipher.encrypt(secret)



#DESXIFRAT
cipher = AES.new(keyhash.digest(), AES.MODE_CFB, iv)
decodedtext = (cipher.decrypt(encodedtext))
print (decodedtext.decode("UTF-8"))  #mostrem la variable com a str
