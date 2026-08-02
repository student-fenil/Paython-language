def pass_list(list):
    max=list[0]
    min=list[0]
    for i in list:
        if i>max:
            max=i
        if i<min:
            min=i
    print(max,min)
    return()
n=int(input("enter no"))
list=[]
for i in range(1,n+1):
    m=int(input("enter element"))
    list.append(m)
print(list)
pass_list(list)

