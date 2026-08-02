i=1
m=1
k=int(input("enter which pattern you wnat to print"))
n=int(input("enter n"))
if(k==1):
    while(i<=n):
        j=1
        while(j<=i):
            print("*",end=" ")
            j+=1
        print()
        i+=1

if(k==2):
    while(i<=n):
        j=1
        while(j<=i):
            print(j,end=" ")
            j+=1
        print()
        i+=1

if(k==3):
    while(i<=n):
        j=1
        while(j<=i):
            print(i,end=" ")
            j+=1
        print()
        i+=1
        
if(k==4):
    while(i<=n):
        sp=1
        while(sp<=n-i):
            print("",end=" ")
            sp+=1
        j=1
        while(j<=i):
            print("*",end=" ")
            j+=1
        print()
        i+=1

if(k==5):
    while(i<=n):
        j=1
        while(j<=i):
            print(m,end=" ")
            j+=1
            m+=1
        print()
        i+=1
        
if(k==6):
    while(i<=n):
        j=1
        l=n
        while(j<=i):
            print(l,end=" ")
            j+=1
            l-=1
        print()
        i+=1

if(k==7):
    while(i<=n):
        j=1
        while(j<=i):
            if(m%2==0):
                print("-1",end=" ")
                j+=1
                m+=1
            else:
                print("0",end=" ")
                j+=1
                m+=1
            print()
            i+=1
            
         
