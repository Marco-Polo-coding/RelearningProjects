"""
Ruleta rusa

1. Se crea un archivo txt con el código de borrar el sistema en cadena de texto
2. Se pregunta al usuario si quiere jugar
	2.1 Si dice que sí, empieza el juego
		2.1.1 Se tiene que elegir un número entra 1 y 6
		2.1.2 Si sale un número distinto al user_choice, el usuario gana
			2.1.2.1 Se pregunta al usuario "¿Quieres ver la pistola?"
				2.1.2.1.1 Si dice que sí se lee el archivo y se muestra el contenido
				2.1.2.1.2 Si dice que no se muestra el "are you sure"
					2.1.2.1.2.1 Si se retracta se vuelve a preguntar sobre si quiere ver la pistola
					2.1.2.1.2.2 Si dice que no se sale del programa
		2.1.3 Si el user_choice es el mismo que el número de la bala se muestra la pantalla de game over
		      y abajo se muestra un "Pulsa una tecla para avanzar..."
		2.1.4 Se pregunta al usuario si quiere jugar otra vez
			2.1.4.1 Si dice que sí se reinicia el juego
			2.1.4.2 Si dice que no se cierra el programa
	2.2 Si dice que no se muestra el ascii "are you sure"
		2.2.1 Si se retracta se reinicia el juego
		2.2.2 Si está seguro se cierra el programa

"""

import random
import os

game_over = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

are_you_sure = """
⠀⠀⠀⠀⠀⠈⠉⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢫⡟⣽⣿⣻⣟⣿⣻⣿⢿
⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣌⠱⡍⢮⡱⢍⠞
⠀⡐⠀⡐⠀⠄⠀⢀⣶⣶⣶⣦⣴⣶⣾⣿⣿⣶⣆⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡁⠠⠁⡐⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠄⢁⠐⠀⠌⠀⣺⡟⠛⠛⢿⣿⡟⠛⠋⣙⣻⣷⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠌⡀⠐⢈⠠⠀⣾⣿⣻⣉⣴⣿⣿⣧⣞⣐⣿⣿⣯⡟⡥⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠂⠄⠁⠂⡀⠀⣼⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠡⠈⠄⡁⢀⠀⠙⣿⣿⣿⡷⠻⠻⠿⣿⣿⣿⣿⣿⡟⠠⠀⠀⠀⠀⠀⠀⠀⡀
⠀⡁⢂⠐⠠⠀⠀⠀⢿⣿⠃⣀⣀⣀⣀⡈⢿⣿⣿⡟⡄⠠⠀⠀⠀⠀⠀⠀⠐⡀
⠀⠡⢈⠐⡀⠄⠀⠀⠸⣽⣶⣿⣟⣻⣿⣷⣼⣿⣿⢳⣥⠠⠀⠀⠀⠀⠀⠀⢂⡁
⠀⠡⢀⠂⠄⢀⠀⠀⢠⡻⣿⣿⣿⣿⣿⣿⣿⢿⣡⣿⣿⠀⠀⠀⠀⠀⠀⠀⠂⠄
⠀⠡⠀⠄⠂⡀⠀⠀⢀⣷⣽⢿⡿⣿⢿⣛⢯⢣⣿⣿⣿⣶⣄⡀⡐⠀
"""

bullet = random.randint(1,6)

# while True: 
    
try:
    if os.path.exists("revolver.txt"):
        os.remove("revolver.txt")
    else:
        print("Beep beep, no se detecta archivo")
        input("Creando...\nPulsa una tecla para continuar.")
    with open("revolver.txt", "x", encoding="utf-8") as f:
        f.write("os.remove(C:\\Program Files)")
except FileExistsError:
    print("revolver.txt existe, abortamos misión.")
    
game_session = input("¿Quieres jugar a la ruleta rusa?: (s/n)\n")

if game_session == "s":
    print("game starts")
elif game_session == "n":
    user_sure = input(are_you_sure+"Are you sure?\n"+"\n(s/n)\n")
    if user_sure == "s":
        print(game_over)
    else: 
        user_sure == "n"
        print("game starts")
    # break

            
    # try:
    #     user_choice = int(input("Escoge un número del 1 al 6: "))
    # except ValueError:
    #     print("Pon un número válido.")
    #     continue
    
    # if bullet == user_choice:
    #     print(game_over)
    # else:
    #     print("You win!")
    #     break
