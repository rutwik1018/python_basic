#clear file and write
f=open("zpractice.txt","w")
f.write("hi goood morning ")
f.close()

#add as it is , in the file
f=open("zpractice.txt","a")
f.write("\n append --->have a nice day \n\n")
f.close()





"""code for how many letters we added in file

f=open("zpractice.txt","w")
a=f.write("i love coding.....!")
print(a)
f.close()
"""