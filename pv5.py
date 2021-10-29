#list and its function
game=["cricket", "football","hockey","chess","baseball","tennis"]
score=[1,4,3,5,7,2,0]
print(game)     #print all elements of list
print("print 0 to 4 == ",game[0:4])  #print 0 to 4
score.sort()    #arrange in sequance
print("after shorting arrange in sequance ==",score)
score.reverse()    #reverd sring
print(" revered string == ",score)
score.insert(2,100)
print("@nd value become the 100",score)

print(game[::-1]) #another way to revered string
game.append("running")
print("after adding ",game)
