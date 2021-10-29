#dictionarynis a key:values pair
dic1={
    "tejas":"tej7",
    "rutik":"rutya",
    "dhoni":"mahi77",
    "rahul":"Rl1",
    "sagar":"saggy79",
    "virat":"viru18",
    "jaddu":{"name":"ravindra jadeja", "call":"sir","num":"33"},
    77:88,
    }

print(dic1)
print(dic1["rahul"])   #print rahul record

print(dic1["jaddu"])   #print jaddu record

print(dic1["jaddu"]["call"])    #print only jaddu

dic1["rohit"]=["hit-man"]     # adding record
dic1[7]=["fav number"]         #adding record also number

print(dic1)    #printind dic1

del dic1[7]      #its delete record 7

dic2=dic1.copy()     #dic1 copy into dic2

print("after copying d2 -->",dic2)