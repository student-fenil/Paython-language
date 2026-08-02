ls=["abc","test","ata"]
ls.sort()
print(ls)
#########################
i=0
ls=[1,2,3,3,2,2,3]
x=int(input("what you want to find"))
cnt=0
while(i<7):
    if ls[i]==x:
        cnt+=1
if cnt==0:
    print("value not found")
else:
    print(cnt)
          
