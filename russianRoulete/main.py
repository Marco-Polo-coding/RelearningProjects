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
        print("El archivo no existe")
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
