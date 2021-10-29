#concepts of sets in python
myset=set(["a","b","c"])
myset2=set(["aa","bb","c","d","g","f"])
print(myset)

myset.add("e")  #adding elelments
myset.add("f")
myset.add("g")

print(myset)  #printing sets

print("diiferance betweemn two set",myset.difference(myset2))   #prints diff betwween two sets

myset2.discard("f")         #remomove f element
print(myset2)