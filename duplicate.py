r=int(input("enter no"))
l=[]

for i in range(1,r+1):
    m=input("enter value") 
    l.append(m)
print(1)

x=[]
for i in l:
    if i not in x:
        x.append(i)
print(x)

