import random 

while True:
    answer= input("Roll the dice? (y/n)?: ")
    
    if answer == "y":
         num1= random.randint(1,5)
         num2= random.randint(1,5)
         print(f"({num1},{num2})")
    elif answer == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid Choice!!")

            