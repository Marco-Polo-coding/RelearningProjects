from horse import *
from race import *

green_horse = Horse("verde")
red_horse = Horse("rojo")
blue_horse = Horse("azul")
yellow_horse = Horse("amarillo")

race = Race(space, lanes)

green_horse_victories = 0
red_horse_victories = 0
blue_horse_victories = 0
yellow_horse_victories = 0

user_correct_guesses = 0

while True:
    def main():
        print("¡Bienvenid@ a la carrera de caballos!")
        print("Los caballos participantes son: verde, rojo, azul y amarillo.")
        user_choice = input("¿Qué caballo crees que ganará? Escribe el color del caballo: ").lower()
        
        '''
        Idealmente debería de empezar
        asignandose cada carril a cada caballo según su color, 
        por ejemplo, caballo verde inicia en x = 0 e Y = 100, así sucesivamente para el resto de caballos, 
        y luego acaban en el máximo de x según su altura fija, la velocidad es aleatoria. 
        El loop acaba cuando uno de los caballos llegue a la meta primero, 
        después se actualiza el contador de victorias del caballo ganador,
        y se actualiza si acierta el usuario el caballo ganador. 
        '''
        # Falta el loop y acabar el resto del código
        winner_horse = "rojo"  # Aquí puedes cambiar el caballo ganador
        
        if user_choice == winner_horse:
            print("¡Felicidades! Has ganado. :-)")
        else:
            print("Lo siento, has perdido. El caballo ganador fue el " + winner_horse + ". :-(")