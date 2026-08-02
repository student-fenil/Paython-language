x="awesome"  #global variable
def myfunc():
    x="fantatstic"
print("python is" + x) #local variable
myfunc() #function call
print("python is"+x) #printing global variable
######################################################
def myfunc():
    global x
    x="fantastic"
myfunc() #function call
print("python is"+x)
###################################################
x="awesome"
def myfunc():
    global x
x="fantastic"
myfunc() #function call
print("python is"+x)
