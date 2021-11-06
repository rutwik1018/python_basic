print("welcome to star pattern : \t\t code-rutvik1018")
print("lets start the game : enter 1 for start pateern  and 0  reveres star-pattern for exit game ")
st_ed=int(input())

if bool(st_ed)==True:
    print("lets start game")
    num=int(input("enter a number for printting star pattern :"))
    for i in range(1,num+1):
        for j in range(i):
            print( " * ",end="")
        print("")


else:
    print("lets start game")
    num = int(input("enter a number for printting star pattern :"))

    for i in range(num+1,0,-1):
        for j in range(i-1):
            print(" * ",end=" ")
        print("")



