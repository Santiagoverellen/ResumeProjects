#Generador de claves aleaotorias 
import string
import random
import subprocess
import platform

def clear_console():
    if platform.system() == "Windows":
        subprocess.run(["cls"], shell=True, check=True)
    else:
        subprocess.run(["clear"], shell=True, check=True)

print("Hola, muchas gracias por utilizar este generador de contraseñas")
lenght = int(input("Ingrese la cantidad de caracteres que quiere que tenga su clave, recuerde que cuantos mas, mayor seguridad\nEl valor puede ir de 8 a 16 por reglas de convencion: "))
while lenght <8 or lenght>16:
    clear_console()
    lenght = int(input("RECUERDA, el numero debe estar entre 8 y 16 por convencion.\nA nadie le gusta que le roben datos, o si? Ingrese el numero: "))
    clear_console()

numbers = 0
upperCase = 0
lowerCase = 0
symbols = 0
password = []

while True:
    numbers = int(input("Ingrese '1' si desea que su clave contenga numeros, o ingrese '0' en caso contrario: "))
    while numbers not in [0, 1]:
        numbers = int(input("No me estas ayudando, tiene que ser '1' o '0': "))
    clear_console()
    upperCase = int(input("Ingrese '1' si desea que su clave contenga letras mayusculas, o ingrese '0' en caso contrario: "))
    while upperCase not in [0, 1]:
        upperCase = int(input("No me estas ayudando, tiene que ser '1' o '0': "))
    clear_console()
    lowerCase = int(input("Ingrese '1' si desea que su clave contenga letras minusculas, o ingrese '0' en caso contrario: "))
    while lowerCase not in [0, 1]:
        lowerCase = int(input("No me estas ayudando, tiene que ser '1' o '0': "))
    clear_console()
    symbols = int(input("Ingrese '1' si desea que su clave contenga simbolos, o ingrese '0' en caso contrario: "))
    while symbols not in [0, 1]:
        symbols = int(input("No me estas ayudando, tiene que ser '1' o '0': "))
    clear_console()
    if numbers == 0 and upperCase == 0 and lowerCase == 00 and symbols == 0:
        print("Me estas pidiendo una contraseña sin caracteres :b  Por favor al menos una condicion tiene que ser afirmativa")
    else:
        break

numbersmodel = string.digits  #Igualo la variable para tener de ejemplo '0123456789'
lowerCasemodel = string.ascii_lowercase  #Igualo la variable para tener de ejemplo 'abcdefghijklmnopqrstuvwxyz'
upperCasemodel = string.ascii_uppercase  #Igualo la variable para tener de ejemplo 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbolsmodel = string.punctuation  #Igualo la variable para tener de ejemplo '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

allowed_values = '' #Declaro esta variable vacia y dependiendo los gustos del usuario, voy agregando informacion
if numbers == 1:
    allowed_values += numbersmodel
if upperCase == 1:
    allowed_values += upperCasemodel
if lowerCase == 1:
    allowed_values += lowerCasemodel
if symbols == 1:
    allowed_values += symbolsmodel

if numbers == 1:                                    #Estoy agregando al menos 1 de cualquiera que el usuario haya pedido
    password.append(random.choice(numbersmodel))    #Total despues puedo hacer un shuffle y lo dejo desordenado
if upperCase == 1:
    password.append(random.choice(upperCasemodel))
if lowerCase == 1:
    password.append(random.choice(lowerCasemodel))
if symbols == 1:
    password.append(random.choice(symbolsmodel))

while len(password) < lenght: #Rellenamos la contraseña segun la longitud del usuario ("Ya que lo minimo eran 8 caracteres")
    password.append(random.choice(allowed_values))

random.shuffle(password) #Aca hago un shuffle sencillo para desordenar la clave

password = ''.join(password) #utilizo el metodo join para convertir password a string, sin dejar espacios entre caracteres

print(f"Esta es tu nueva contraseña totalmente aleatoria, espero resguarde muy bien tu informacion\n---->\t{password}\t<----")