AryaVSMargaret=input("Enter a number, then space, then another number... ")
AryaMargaret=AryaVSMargaret.split( )

def InRange(Arya,Margaret):
    if Arya<0 or Arya>10**9 or Margaret<0 or Margaret>10**9:
        print("Invalid values")
    else:
        StartChecker(Arya,Margaret)

def StartChecker(Arya,Margaret):
    if Arya==Margaret:
        print("Depends on who starts...")
    else:
        if Arya>Margaret:
            print("Margaret will think of something.")
        else:
            print("Arya will think of something.")

print("Arya's Programs: "+str(AryaMargaret[0])+".")
print("Margaret's Algorithms: "+str(AryaMargaret[1]+"."))

InRange(int(AryaMargaret[0]),int(AryaMargaret[1]))