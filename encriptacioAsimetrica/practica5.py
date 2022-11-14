#import
from Crypto.PublicKey import RSA

#########################################################
#                GENERACIÓN DE LA CLAVE                 #
#########################################################

# Generar pareja de claves RSA de 2048 bits de longitud
key = RSA.generate(2048)

# Passphrase para encriptar la clave privada
secret_code = "12345"

# Exportamos la clave privada
private_key = key.export_key(passphrase=secret_code)

# Guardamos la clave privada en un fichero
with open("private.pem", "wb") as f:
    f.write(private_key)

# Obtenemos la clave pública
public_key = key.publickey().export_key()

# Guardamos la clave pública en otro fichero
with open("public.pem", "wb") as f:
    f.write(public_key)
# fer-ho amb rsa
# cr ar parells de claus i xifrar/desxifrar documents
# funcions independents sense variables globals
# 1. una funcio que escrigui a un fitxer una clau publica
# 2. una funcio que llegeixi la clau publica 
# 3. una funcio que xifra(clau, text)
# 4. una funcio que desxifra(clau, text)
# 5. una funcio que executi un exemple de funcionament en mode consola

