i=1
n=3
while(i<=n):
    j=1
    while(j<=i):
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
#####################################
i=1
n=int(input("enter n"))
while(i<=n):
    sp=1
    while(sp<=n-i):
        print(" ")
        sp+=1

        j=1
        while(j<=i):
            print("*")
            j+=1
        print()
        i+=1
        
