while True:
    user_input= input("Do you want to play? (yes/no): ")
    if user_input == "yes":
        try:
            number= int(input("Enter number: "))
            if number % 2 == 0:
                print("Even")
            else:
                print("Odd")
        except ValueError:
            print("Invalid, Enter a number.")
    else:
        break