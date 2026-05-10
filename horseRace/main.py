from horseRace.horse import *
from horseRace.race import *

# Initialize the horses with their respective colors and starting positions
green_horse = Horse("verde", lanes['verde']['start_x'], lanes['verde']['y'])

red_horse = Horse("rojo", lanes['rojo']['start_x'], lanes['rojo']['y'])

blue_horse = Horse("azul", lanes['azul']['start_x'], lanes['azul']['y'])    

yellow_horse = Horse("amarillo", lanes['amarillo']['start_x'], lanes['amarillo']['y'])

race = Race(space, lanes)



# Main function to run
def main():
    
    # Initialize victory counters and user guesses
    green_horse_victories = 0
    red_horse_victories = 0
    blue_horse_victories = 0
    yellow_horse_victories = 0
    user_correct_guesses = 0
    
    while True:
        # Welcome message and user input
        print("¡Bienvenid@ a la carrera de caballos!")
        print("Los caballos participantes son: verde, rojo, azul y amarillo.")
        user_choice = input("¿Qué caballo crees que ganará? Escribe el color del caballo: ").lower()
        
        # List of horses and the winner variable in null before the race
        horses = [green_horse, red_horse, blue_horse, yellow_horse]
        winner_horse = None
        
        # Reset the position of each horse to the starting line before
        for horse in horses:
            horse.x = 0  
                    
        # Loop to simulate the race
        while not winner_horse:
            # Move each horse at random speeds and check if any has reached the finish line
            for horse in horses:
                horse.speed = random.randint(1, 10)
                horse.x += horse.speed  # Mover el caballo según su velocidad
                if horse.x >= lanes[horse.color]['finish_x']:
                    winner_horse = horse.color
                    break
        
        # Update victory counters based on the winner
        if winner_horse == "verde":
            green_horse_victories += 1
        elif winner_horse == "rojo":
            red_horse_victories += 1
        elif winner_horse == "azul":
            blue_horse_victories += 1
        elif winner_horse == "amarillo":
            yellow_horse_victories += 1

        # Check if the user's guess was correct and update the correct guesses counter
        if user_choice == winner_horse:
            user_correct_guesses += 1
            print("¡Felicidades! Has ganado. :-)")
        else:
            print("Lo siento, has perdido. El caballo ganador fue el " + winner_horse + ". :-(")
        print("Victorias por caballo:")
        print("Verde: " + str(green_horse_victories))
        print("Rojo: " + str(red_horse_victories))
        print("Azul: " + str(blue_horse_victories))
        print("Amarillo: " + str(yellow_horse_victories))
        print("Aciertos del usuario: " + str(user_correct_guesses))
        nueva_ronda = input("\n¿Quieres jugar otra vez? (s/n) ").lower()


        if nueva_ronda != "s":
            break

if __name__ == "__main__":
    main()