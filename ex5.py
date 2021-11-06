
print("Welcome to stone paper scissor game ")
print("You havr to win at least 3 round out of 5 round")
score=0

for i in range(1,6):

    import random
    computer_turn=random.randrange(1,4,1)
    print("Choose: 1 -- rock   2 -- paper    3 -- scissor ")
    your_turn=int(input())
    if   your_turn==1 and  computer_turn==3:
        print("you are wineer ....!")
        score=score+1
    elif your_turn ==2 and computer_turn==1:
        print("you are wineer ....!")
        score = score + 1
    elif  your_turn == 3 and computer_turn==2:
         print("you are winnier")
         score = score + 1

    elif computer_turn ==  your_turn:
        print("match tied")
    else:
        print("computer winner...!")

print("  your score score ===  ",score,"/5")