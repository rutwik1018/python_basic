# for loops
# enter a number for printing table and its star pattern
print("welcome to for loops :")
num=int(input("enter number for table:"))

for i in range(1,11):
    ans=num*i
    print( num ," * ", i," = ",ans)
    i=i+1



#star pattern code
print("\n\n star pattern : ")
for j in range(1,num+1):
    for x in range(j):
        print(" * ", end =" ")
    print(" ")