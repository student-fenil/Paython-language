n=int(input("enter number of elements:"))
ls=[]
for i in range(n):
    num=int(input("enter element"))
    ls.append(num)
ls.sort()
print("ascending order list:")
print(ls)

