#tell() and seek() functions
#
f=open("zpractice.txt")          #opening the file
print("we are at position --> ", f.tell())      # getting position
print(f.readline())                             #reading line
print("now we are at --> ",f.tell())            # getting position


f.seek((5))     #set position at 5th letter
print("going to 5th position --> ",f.tell())