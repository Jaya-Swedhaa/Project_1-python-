# comprehension with mannually given list

list1 = ["app","web","lap","portal","stack","cooler"]
newlist =[x for x in list1 if "a" in x]
newlist1 =[x.upper() for x in list1]
print(newlist)
print(newlist1)

# creating a list and updating to new list

listt=[]
for i in range(5):
    listt.append(i)
print(listt)
newlist=[x*2 for x in listt]
print(newlist)

# creating the comprehension with the presence of condition
newlist=[x for x in range(10) if x>5 and x%2==0]
print(newlist)

# creating comprehension in strings

newlistt =[x.upper() for x in "Python"]
print(newlistt)