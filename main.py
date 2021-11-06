 # itretive and recursive function

def facto_itretive(n):
     fact=1
     for i in range(1,n+1):
         fact=fact*i
     return fact




def facto_recursive(n):
    if n==1:
        return 1
    else:
        return n* facto_recursive(n-1)

#-------------------------------------------
n=int(input("enter a number : "))
print("factorial using itretive function == ", facto_itretive(n))
print("factorial using rec function == ", facto_itretive(n))