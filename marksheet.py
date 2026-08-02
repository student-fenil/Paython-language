n=int(input("enter student name:"))
r=int(input("enter roll number"))
p=float(input("enter percentage"))
if p>90:
    print("distiction")
elif p>80:
    print("first class")
elif p>70:
    print("second class")
elif p>60:
    print("third class")
elif p>33:
    print("pass class")
else:
    print("fail")
