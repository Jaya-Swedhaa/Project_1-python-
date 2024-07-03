#try except

x="chennai"
try:
 print(x)
except:
 print("an exception occured")

 #Many exception

x="delhi"
try:
 print(x)
except NameError:
 print("an exception occured")
except:
 print("something else went wrong")

#try else exception

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("no error")

#finally method

try:
    print("hello")
except:
    print("something went wrong")
finally:
    print("error handling over")

#raise method

PE=10
IPE=8
if PE>IPE:
    raise Exception("Overvalued")