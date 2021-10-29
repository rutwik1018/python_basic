#if else statements study

var1=int(input("enter a number:"))

if var1>=75:
     print("you got firs tclass with dict")
elif var1>=60:
    print("u got first class")
elif var1>=50:
    print("you god second class")
elif var1>=40:
    print("you got third class")
else:
    print("you fail")

#----------------------list
print("\n\n ----------list with if elif----------")
list1=[1,2,3,4,5,6,7,8,9,0,]
print( 5 in list1)
print(5 not in list1)

if 7 in list1:
    print("yes 7 number is in list")