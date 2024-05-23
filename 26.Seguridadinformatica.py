from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import secrets

# Función para cifrar un mensaje utilizando AES
def cifrar(mensaje, clave):
    cifrador = AES.new(clave, AES.MODE_GCM)
    nonce = cifrador.nonce
    cifrado, tag = cifrador.encrypt_and_digest(mensaje.encode())
    return cifrado, nonce, tag

# Función para descifrar un mensaje utilizando AES
def descifrar(cifrado, clave, nonce, tag):
    descifrador = AES.new(clave, AES.MODE_GCM, nonce=nonce)
    mensaje = descifrador.decrypt_and_verify(cifrado, tag)
    return mensaje.decode()

# Función para hashear una contraseña utilizando SHA-256
def hashear_contrasena(contrasena, salt):
    contrasena_salt = contrasena.encode() + salt
    hashed_contrasena = hashlib.sha256(contrasena_salt).hexdigest()
    return hashed_contrasena

# Función para generar un salt aleatorio
def generar_salt():
    return secrets.token_bytes(16)

# Función para generar un pepper fijo
def generar_pepper():
    return b'mi_pepper_secreto'

# Función para verificar una contraseña hasheada con salt y pepper
def verificar_contrasena(contrasena_ingresada, salt, pepper, hashed_contrasena):
    contrasena_salt_pepper = contrasena_ingresada.encode() + salt + pepper
    hashed_contrasena_verificada = hashlib.sha256(contrasena_salt_pepper).hexdigest()
    return hashed_contrasena == hashed_contrasena_verificada

# Ejemplo de uso
mensaje_original = "Este es un mensaje secreto"
clave = get_random_bytes(16)  # Clave de 16 bytes para AES
contrasena = "mi_contrasena_secreta"

# Cifrar el mensaje
cifrado, nonce, tag = cifrar(mensaje_original, clave)

# Hashear la contraseña con salt
salt = generar_salt()
hashed_contrasena = hashear_contrasena(contrasena, salt)

# Verificar la contraseña
pepper = generar_pepper()
if verificar_contrasena(contrasena, salt, pepper, hashed_contrasena):
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")

# Descifrar el mensaje
mensaje_descifrado = descifrar(cifrado, clave, nonce, tag)

print("Mensaje original:", mensaje_original)
print("Mensaje cifrado:", cifrado)
print("Mensaje descifrado:", mensaje_descifrado)
print("Salt:", salt)
print("Contraseña hasheada con salt y pepper:", hashed_contrasena)

