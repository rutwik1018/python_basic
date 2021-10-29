 #fuctions in python




print("\t adding numbers useing the fuction:")
print("enter a first number: ")
a=int(input())
print("enter a second number : ")
b=int(input())

c=sum((a,b))    #built in function
print("sum of two number using built in function : --> ",c)


#user defined fuction
def additions_ab(a,b):
    print("addition of number using user-defined fuction :--> ")
    c=a+b
    print("additon== ",c)

additions_ab(a,b)   #fuction calling


# return type fuction
def multiplication_return(a,b):
    mul=a*b
    return mul

d=multiplication_return(a,b)
print("the multiplication using return type fuction :--> " ,d)
