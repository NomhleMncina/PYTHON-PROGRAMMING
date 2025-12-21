
score=0
Question_one = input("What is the green pigment fount in leaves? ")
if Question_one == "Chlorophyl":
    print("Correct")
    score= score + 1
else:
    print("Wrong")

Question_twoo = input("One plus three is four? ")
if Question_twoo == "True":
    print("Correct")
    score= score + 1
else:
    print("Wrong")

Question_three = input("CPU stand for random access memory? ")
if Question_three == "False":
    print("Correct")
    score= score + 1
else:
    print("Wrong")

Question_four = input("ID number has 10 digits? ")
if Question_four == "False":
    print("Correct")
    score= score + 1
else:
    print("Wrong")

Question_five = input("South Arica is a Country? ")

if Question_five == "True":
    print("Correct")
    score= score + 1
else:
    print("Wrong")


print(f"You got {score}")

