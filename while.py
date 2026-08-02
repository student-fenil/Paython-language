i=1
sum=0
while(i<=5):
    print(i)
    sum=sum+i
    i=i+1
print(sum)
####################################################

i=1
n=5
while(i<=n):
    if i%2==0:
        print(i*i,end=" ")
    else:
        print(i,end=" ")
    i=i+1
#####################################################
i=1
n=int(input("enter n"))
while(i<=n):
    if i%2==0:
        print("-1",end=" ")
    else:
        print("0",end=" ")
    i=i+1
