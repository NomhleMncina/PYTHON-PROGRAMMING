vowels= "aeiou"
name= input("Enter name: ")
count=0

for char in name:
    if char in vowels:
       count= count + 1
       print(f"{name} has {count} vowels",)
    else:
        quit


