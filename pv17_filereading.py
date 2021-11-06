#file reading

file_var=open("pv1.py")    #file_var is variable
read_var=file_var.read()   #read var is variable where all lines store
print(read_var)            #printing file text
file_var.close()           #closing file

#2nd way to read files to read only 50 letters
""" file_var=open("pv1.pv",rt)
    read_var=f.read(50)
    print(read_var)
 file_var.close()
 
 #3rdway to read and store in list
  file_var=open("pv1.pv",rt)
  print(f.readlines())
 file_var.close()
 """