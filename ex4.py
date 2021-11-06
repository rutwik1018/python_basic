my={1:'Harry',2:'Rohan',3:'Hammad'}
you={1:'Exercise',2:'Diet'}
def getdate():
    import datetime
    return datetime.datetime.now()
def function1():
    print("Do you want to log or retrieve?")
    c = int(input("Press 1 for log,2 for retrieve\n"))
    if c==1:
        print("Which client do you want to log for?")
        a=int(input("Press 1 for Harry,2 for Rohan,3 for Hammad\n"))
        print("What do you want to log for?")
        b=int(input("Press 1 for Exercise,2 for Diet\n"))
        if b==1:
            with open(my[a]+you[b]+".txt","a") as e:
             k=input("Which Exercise did you do?\n")
             e.write(str([str(getdate())])+"-"+k+"\n")
             print("Successful")
        elif b==2:
            with open(my[a]+you[b]+".txt","a") as f:
             m=input("What did you eat?\n")
             f.write(str([str(getdate())])+"-"+m+"\n")
             print("Successful")
    elif c==2:
        print("Which client do you want to retrieve for?")
        r=int(input("Press 1 for Harry,2 for Rohan,3 for Hammad\n"))
        print("What do you want to retrieve?")
        s=int(input("Press 1 for Exercise,2 for Diet\n"))
        if s==1:
            with open(my[r] + you[s] + ".txt") as g:
                content=g.read()
                print(content)
        elif s==2:
            with open(my[r] + you[s] + ".txt") as h:
                body=h.read()
                print(body)
function1()


def getdate():
    import datetime
    return datetime.datetime.now()

def append(client):
    d = int(input("Choose Log type\n1 for 'Diet'\n2 for 'Exercise'"))
    if d == 1:
        with open(client + "diet.txt", "a") as file:
            en = input("enter your Diet\n")
            file.write("[" + str(getdate()) + "]: " + en + "\n")
    elif d == 2:
        with open(client + "ex.txt", "a") as file:
            en = input("enter your Exercise\n")
            file.write("[" + str(getdate()) + "]: " + en + "\n")

def read(client):
    d = int(input("What you want to retrieve\n1 for 'Diet'\n2 for 'Exercise'"))
    if d == 1:
        with open(client + "diet.txt") as file:
            p = file.read()
            print(p)
    elif d == 2:
        with open(client + "ex.txt") as file:
            p = file.read()
            print(p)
    return p

print("Health Management System")
inp = int(input("Choose your client"
                "\n1 for 'Harry'"
                "\n2 for 'Rohan'"
                "\n3 for 'Hammad'"
                ))
cl2 = int(input("1 for 'Log'\n2 for 'Read'"))
Client = ''
if inp == 1:
    Client = "Harry"
elif inp == 2:
    Client = "Rohan"
elif inp == 3:
    Client = "Hammad"
if cl2 == 1:
    append(Client)
elif cl2 == 2:
    read(Client)