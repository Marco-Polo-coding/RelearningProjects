import random

while True:
    random_choice = random.randint(1,10)
    user_choice = int(input("Guess the number: "))
    if user_choice == random_choice:
        print("You're correct")
        break
    else:
        print("Try again")
        
        

