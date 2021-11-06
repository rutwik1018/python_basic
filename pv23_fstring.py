#fstring study
name=input("enter your name : ")
age=int(input("enter your age : "))

number="my name is %s"%name
print(number)


print("---------2nd way ------------")
a= "my name is {0} and my age is {1} "
# a="my name is {name} and my age is {age}"
b=a.format(name,age)
print(b)


print("third way-----------------------")
num=f"this is {name} and hus age {age} and after\n\t 10 years his age{ age + 10}"
print(num)