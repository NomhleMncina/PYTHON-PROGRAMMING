import random


while True:
    emojis={"r":"🪨", "p":"📄","s":"✂️"}
    guesses=("r","p","s")
    try:
        user_guess= input("Rock, Paper or Scissors? (r/p/s): ")
        computer= random.choice(guesses)
        print(f"you chose {emojis[user_guess]}")
        print(f"computer chose {emojis[computer]}")

        if(user_guess == "r" and computer == "s") or (user_guess == "p" and computer == "r") or (user_guess == "s" and computer == "p"):
            print("You win")
        elif user_guess == computer:
            print("tie")
        else:
            print("Ooops! you loose")

        wanna_continue= input("Do you want to continue? (y/n): ")

        if wanna_continue == "n":
            break
        else:
            continue

               
    except KeyError:
        print("Invalid Guess!!")
    
    