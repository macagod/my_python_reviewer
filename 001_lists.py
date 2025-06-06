# Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"] 
print(mylist) # ['banana', 'cherry', 'apple']

mylist2 = [5, True, "apple", "apple"]
print(mylist2) # [5, True, 'apple', 'apple']

item = mylist[0]
print(item) # banana

item = mylist[-1]
print(item) # apple

for x in mylist:
    print(x) # banana, cherry, apple

if "banana" in mylist:
    print("yes")
else:
    print("no") # yes

print(len(mylist)) # 3

mylist.append("lemon")
print(mylist) # ['banana', 'cherry', 'apple', 'lemon']

mylist.insert(1, "blueberry")
print(mylist) # ['banana', 'blueberry', 'cherry', 'apple', 'lemon'] 

mylist.remove("cherry")
print(mylist) # ['banana', 'blueberry', 'apple', 'lemon']

mylist.pop()
print(mylist) # ['banana', 'blueberry', 'apple']    

mylist.pop(0)
print(mylist) # ['blueberry', 'apple']

mylist.clear()
print(mylist) # []  


