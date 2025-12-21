To_Do_List=["Cook","Wash","Clean","Study"]
while True:
    user_input= input("Do you want to add/view/remove task? (add/view/remove): ")

    if user_input == "view":
        for i in To_Do_List:
            print(i)
    elif user_input == "remove":
        to_remove= input("What do you want to remove?: ")
        if to_remove in To_Do_List:
            To_Do_List.remove(to_remove)
            print(To_Do_List)
        else:
            print("Not Found!!")
    elif user_input == "Add":
        to_add= input("What do you want to add?: ")
        To_Do_List.append(to_add)
        print(To_Do_List)
    else:
        break