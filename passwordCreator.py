import random
import os
import sys
import string
#Longitud de la contraseña
print("Establezca el tamaño de la contraseña:")
tam=input("Por defecto es aleatorio, con una longitud entre 8 y 32 carácteres:\n")
#En caso de no interpretar lo que introduce el usuario, se escoge una longitud aleatoria entre 8 y 32 caracteres
if tam=="" or not tam.isnumeric():
    print("Longitud aleatoria\n")
    tam=random.randint(8,32)
#Símbolos extraños: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
sim=input("¿Desea símbolos extraños? [S/n]\n")
#Tam es string por introducirse por input. En caso de ser el string original, se pasa a int
tam=int(tam)
#Se comprueba si se desean símbolos extraños y genera las contraseñas en consecuencia
if sim=="" or sim=="S" or sim=="s":
    randomstr = ''.join(random.choices(string.ascii_letters+string.digits+string.punctuation+"ñ"+"@"+" ",k=tam))
else:
    randomstr = ''.join(random.choices(string.ascii_letters+string.digits,k=tam))
#Imprime por pantalla la contraseña generada
print(randomstr)
