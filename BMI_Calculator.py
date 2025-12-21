def main():
    weight= float(input("How much do you weigh?: "))
    Height= float(input("How tall are you?: "))
    print(bmi(weight,Height))

def bmi(weight,Height):
    height= Height * Height
    bmi= weight / height
    return bmi
    
main()