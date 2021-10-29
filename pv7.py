#clear concept of dictionary
#creaate dictionary and search words in it ,word input from user
dic={
    "sachin":"god of cricket",
    "sewagh":"powerful opener",
    "youraj":"match winner ",
    "dhoni":"kingmaker for india",
    "virat":"run machine",
    "rohit":"hitman",
    "jadeja":"beast allRounder",
    "rahul":"classical shots",
      }

print("chooses the one player to know his quality or nikename:- ",dic.keys())

inp=input("\nplayer name::-->")      #taking input

print(dic[inp])


print(dic.keys())