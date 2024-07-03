"""x="chennai"
try:
 print(x)
except:
 print("an exception occured")

x="delhi"
try:
 print(x)
except NameError:
 print("an exception occured")
except:
 print("something else went wrong")

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("no error")

try:
    print("hello")
except:
    print("something went wrong")
finally:
    print("error handling over")"""

PE=10
IPE=8
if PE>IPE:
    raise Exception("Overvalued")
else:
    print("no issues")