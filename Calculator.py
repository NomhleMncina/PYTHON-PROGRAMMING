def main():
    while True:
        x=int(input("Enter first number: "))
        operator= input("Enter Operator: ")
        y=int(input("Enter second number: "))
        
        if operator == "+":
            print(addition(x,y))
        elif operator == "-":
            print(substraction(x,y))
        elif operator == "/":
            print(division(x,y))
        elif operator == "*":
            print(multiplication(x,y))
        else:
            print("Invalid Sign!!")
        
        proceed= input("Do you want to continue counting? ") 

        if proceed == "n":
            break   
        else:
            continue
 
def addition(x, y):
    sum= x + y
    return sum

def substraction(x, y):
    difference= x - y
    return difference

def multiplication(x, y):
    product= x * y
    return product

def division(x, y):
    cocience= x / y
    return cocience

main()



