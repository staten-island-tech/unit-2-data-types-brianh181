Eastbound=input("Eastbound: yes or no? ")
Westbound=input("Westbound: yes or no? ")

def traffic(East,West):
    if not East == "yes" and not East == "no" or not West == "yes" and not West == "no":
        print("ERROR")
    else:
        if East == "yes":
            if West == "yes":
                print("not possible")
            else:
                print("possible")
        else:
            if West == "no":
                print("Tunnel is empty")
            else:
                print("possible")

traffic(Eastbound,Westbound)