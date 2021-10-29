print("WELCOME..... \n Number guessing game: \t\t\t\t code by-rutvik18")
print("\tGuess number in 9 chances : ")
secret_number=18
chances=1
print("\nLET's START THE GAME:")

while(chances<=9):
    print("\nGuess the number::")
    user_inp=int(input())
    if user_inp >=65:
        print( user_inp,"is a big number ,plzzz guess small number !")
    elif user_inp >18:
        print(user_inp,"is biger number")
    elif user_inp <18:
        print(user_inp,"is smaller number")
    else:
        print("congratulation....! you won in ", chances, " chances ")
        break
    print(9-chances,"  Chances left:")
    chances=chances+1

if(chances>9):
    print("game over ...... better luck next time ")