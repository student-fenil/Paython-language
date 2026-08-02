ch="y"
print("1. skip")
print("2. reverse")
print("3. length")
str=input("enter string")
while(ch=="y"):
    c=int(input("enter choice for menu"))
    if(c==1):
        print(str[::2])
    elif(c==2):
        print(str[::-1])
    elif(c==3):
        print(len(str))
    else:
        print("enter valid value")
     # ch=input("enter y/n")

