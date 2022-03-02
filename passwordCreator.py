import random
import os
import sys
import string
print("Establezca el tamaño de la contraseña:")
tam=input("Por defecto es aleatorio, con una longitud entre 8 y 32 carácteres:\n")
if tam=="" or not tam.isnumeric():
    print("Longitud aleatoria\n")
    tam=random.randint(8,32)
sim=input("¿Desea símbolos extraños? [S/n]\n")
tam=int(tam)
if sim=="" or sim=="S" or sim=="s":
    randomstr = ''.join(random.choices(string.ascii_letters+string.digits+string.punctuation+"ñ"+"@"+" ",k=tam))
else:
    randomstr = ''.join(random.choices(string.ascii_letters+string.digits,k=tam))
print(randomstr)
