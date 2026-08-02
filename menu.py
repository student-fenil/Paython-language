list1=[1,2,3]
true=[0]
while true:
    print("menu for list")
    print("1. add element") 
    print("2. delete")
    print("3. replace")
    print("4. insert")
    print("5. sort")
    print("6. print")
    print("7. exit")

    ch=int(input("enter choice"))

    if ch==1:
        n=int(input("enter element"))
        list1.append(n)

    elif ch==2:
        n=int(input("enter element deleted"))
        list1.remove(n)

    elif ch==3:
        a=int(input("enter replaced position"))
        b=int(input("enter element value"))
        list1[a]=b

    elif ch==4:
        a=int(input("enter inserted position"))
        b=int(input("enter element value"))
        list1.inset(a,b) 

    elif ch==5:
        list1.sort()

    elif ch==6:
        print(list1)

    elif ch==7:
        break

    else:
        print("invalid choice")


