import random
import os
import sys
contraseña=""
long=int(input("Introduce la longitud deseada de contraseña:\n"))
for i in range(0,long):
    ran=random.randint(32,254)
    if ran==127:
        i=i-1
        continue
    letra=chr(ran)
    contraseña=contraseña+letra
    print(str(ran)+" "+letra)
print(contraseña)