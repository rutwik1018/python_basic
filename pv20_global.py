
x=10   #global variable
def func1():
    x = 20  #local variable
    def fucn2():
        global x             #permission to make global variable
        x = 1000            #becomes global variable and change it
    fucn2()
    print("value of x after calling func1() --> ",x)


func1()
print("value after global ---> ",x)