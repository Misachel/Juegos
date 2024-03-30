from random import *

print("Hola bienvenido al juego de adivina el número... O_o")
print("\n")

nombre = input("Dime, cual es tu nombre: ")
print(f"Que tal {nombre} espero estes listo para este juego \n")

print(f"{nombre}... He pensado en un número del 1 al 100 tendras 8 oportunidades para adivinar mi número... U.U \n")

intentos = 0
numero = 0
num_adv = randint(0,100)

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres comenzar el juego... :)? s/n \n")

    while intentos < 8:
        numero = int(input("Cuál es el número?: "))
        intentos += 1

        if numero < num_adv:
            print("Mi numero es mas alto")
        elif numero > num_adv:
            print("Mi numero es mas bajo")
        else:
            print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
            break
    if numero != num_adv:
        print(f"Lo siento, se han agotado los intentos. El numero secreto era {num_adv}")
else:
   print("Lastima, espero vuelvas pronto :(...")
