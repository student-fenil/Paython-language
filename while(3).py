####################################
i=1
n=int(input("enter n"))
m=65
while(i<=n):
    if i%2==0:
        print(i,end==" ")
    else:
        print(chr(m),end=" ")
        m+=1
        i+=1
#####################################

k=65
print(chr(k))
k=k+1
print(chr(k))
