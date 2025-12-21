Data={"Nomhle":24,"Aviwe":3,"Cat":90}

Name= input("Enter name: ")

if Name in Data:
    print(f"{Name} id {Data[Name]} years old")
else:
    print("Not Found")