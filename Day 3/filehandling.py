#removing the file

import os 
os.remove("myfile.txt")

#creating file

f=open("myfile.txt","x")

# writing in the created file

f=open("myfile.txt","w")
f.write("Providing value is more important. Value is given by the information we are providing. ")
f.writelines(["adutha line\n"])
f.close()

#adding content using append method

f=open("myfile.txt","a")
f.write("In short value in information is important.")
f.close()

# reading the file

f=open("myfile.txt","r")
print(f.read())
print(f.read(7))

