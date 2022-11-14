from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA



#########################################################
#                        CIFRADO                        #
#########################################################
# Cadena UTF-8 a encriptar
cadena = "Hola StackOverflow en español"

# Trabajamos con bytes, codifcamos la cadena.
bin_data = cadena.encode("utf-8")

# Leemos el archivo con la clave publica
with open("public.pem", "rb") as f:
    recipient_key = f.read()

# Cargamos la clave pública (instancia de clase RSA)
key = RSA.importKey(recipient_key)

# Instancia del cifrador asimétrico
cipher_rsa = PKCS1_OAEP.new(key)

# Encriptamos la cadena usando la clave pública
enc_data = cipher_rsa.encrypt(bin_data)

print(enc_data)
# b'l;\xc7\x96\xbd\xb5:\xb8:\xf0\xdc\xa6b\xbd)\xf7xb4\xca\xf0~\x0b...'

#########################################################
#                       DESCIFRADO                      #
#########################################################

# Leemos el archivo con la clave privada
with open("private.pem", "rb") as f:
    recipient_key = f.read()

# Cargamos la clave privada (instancia de clase RSA)
key = RSA.importKey(recipient_key, passphrase="12345")

# Instancia del cifrador asimétrico
cipher_rsa = PKCS1_OAEP.new(key)

# Desencriptamos la cadena usando la clave privada
dec_data = cipher_rsa.decrypt(enc_data)

# Decodificamos la cadena
cadena = dec_data.decode("utf-8")

print(cadena)
# "Hola StackOverflow en español"

