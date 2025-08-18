x=5
if(type(x) is int):
    print("true")
else:
    print("false") 

x=5.0
if(type(x) is not float):
    print("true")
else:
    print("false")

x=20
y=20
if x is y:
    print("true") 
else:
    print("false")               

a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=a
print(a in c)
print(a not in b)

