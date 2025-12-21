import random
number= random.randint(0,10)
count=0

while True:
    try:
        user_input= int(input("Enter a number between 1 and 10: "))
        
        if user_input == number:
            count += 1
            print(f"Congrats!! you got {number}")
            print(f"you got it in {count} tries")
            break
        elif user_input > number:
            count += 1
            print("Too high")
        else:
            print("Too low")
            count += 1
    except ValueError:
        print("Invalid! please enter a number")