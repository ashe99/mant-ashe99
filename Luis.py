"""def darmensaje(mensaje):
   print ("Hola Mundo!!!", mensaje)

darmensaje("Pablo")"""

"""#Science Data

def PatternCount(Text, Pattern):
    count = 0
    
    for i in range(len(Text)):

        if Text[i:i+len(Pattern)] == Pattern:
            count+=1
    return count

Text = "GCGCGC"
Pattern = "GCG"
print(PatternCount(Text, Pattern))"""

#Generador de Contraseña/Longitud pre-establecida

import random
import string


def genaratePassword():

    rango =list(range(4,16))
    longitud=random.choice(rango)
    caract=string.ascii_letters+string.digits+string.punctuation
    contraseña=("").join(random.choice(caract)for i in range(longitud))
    print("Contraseña Creada: ",contraseña)

genaratePassword()



