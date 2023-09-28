number1=int(input("Please input a number... "))
number2=int(input("Please input another number... "))

def listFactors(number1,number2):
    checkFactorNumber=1
    Common_factors=[]
    GreaterNumber=0

    if number1 > number2:
        GreaterNumber=number1
    else:
        GreaterNumber=number2

    for i in range(GreaterNumber):
        if number1 % checkFactorNumber == 0 and number2 % checkFactorNumber == 0:
            Common_factors.append(checkFactorNumber)
            print(checkFactorNumber)
        checkFactorNumber += 1

    print("The common factors for "+str(number1)+" and "+str(number2)+" are "+str(Common_factors)+".")

    Gcf=len(Common_factors)-1
    Gcf=Common_factors[Gcf]

    print("The GCF is "+str(Gcf)+".")
    

listFactors(number1,number2)
