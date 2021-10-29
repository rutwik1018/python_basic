#task --> create faulty calculator
"""
design a calculator which will correctly solve all the problems
but answer for this  --> 1)45*3=555    2)56+9=77      3)56/6=4   4)50-2=999
"""

print("welcome to faulty calculator :desing by --> rutvik adhalrao")
op=input("\tchoose oprationn:")
num1=int(input("enter a first number:"))
num2=int(input("enter a second number"))

if op=="*":

    if num1== 45 and num2 ==3:
        print("multiplication = 555")
    else:
         print("multiplication = ",num1*num2)

elif op =="+":
    if num1== 56 and num2 ==9:
        print("adddition  = 77")
    else:
         print("addition = ",num1+num2)

elif op=="/":
    if num1==56 and num2 ==6:
        print("division = 4")
    else:
        print("division = ",num1/num2)

elif op=="-":
    if num1==50 and num2== 20:
          print("subtraction =  999")
    else:
          print("subtraction = ",num1-num2)


else:
    print("please choose only / * - and + ")




