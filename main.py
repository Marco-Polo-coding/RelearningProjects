from horse import *
from race import *

green_horse = Horse("verde", lanes['verde']['start_x'], lanes['verde']['y'])

red_horse = Horse("rojo", lanes['rojo']['start_x'], lanes['rojo']['y'])

blue_horse = Horse("azul", lanes['azul']['start_x'], lanes['azul']['y'])    

yellow_horse = Horse("amarillo", lanes['amarillo']['start_x'], lanes['amarillo']['y'])

race = Race(space, lanes)




def main():
    green_horse_victories = 0
    red_horse_victories = 0
    blue_horse_victories = 0
    yellow_horse_victories = 0
    user_correct_guesses = 0
    
    print("¡Bienvenid@ a la carrera de caballos!")
    print("Los caballos participantes son: verde, rojo, azul y amarillo.")
    user_choice = input("¿Qué caballo crees que ganará? Escribe el color del caballo: ").lower()
    
    horses = [green_horse, red_horse, blue_horse, yellow_horse]
    winner_horse = None  # Aquí puedes cambiar el caballo ganador
    
    while not winner_horse:
        for horse in horses:
            horse.speed = random.randint(1, 10)
            horse.x += horse.speed  # Mover el caballo según su velocidad
            if horse.x >= lanes[horse.color]['finish_x']:
                winner_horse = horse.color
                break
        
    if winner_horse == "verde":
        green_horse_victories += 1
    elif winner_horse == "rojo":
        red_horse_victories += 1
    elif winner_horse == "azul":
        blue_horse_victories += 1
    elif winner_horse == "amarillo":
        yellow_horse_victories += 1

    if user_choice == winner_horse:
        user_correct_guesses += 1
        print("¡Felicidades! Has ganado. :-)")
    else:
        print("Lo siento, has perdido. El caballo ganador fue el " + winner_horse + ". :-(")
               

if __name__ == "__main__":
    main()