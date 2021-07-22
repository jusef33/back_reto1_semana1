#Reto 1: Desarrollar un programa de bienvenid

import datetime

edad = int(input("ingresa tu edad "))

hora= int(datetime.datetime.now().strftime('%H'))

if edad < 18: 
    if(hora > 18):
        print ("Vaya a dormir")
    else:
        print("Haga su tarea.")
else:
    print("No estas obligado a hacer nada.")