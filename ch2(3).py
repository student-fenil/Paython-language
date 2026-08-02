def my_function():
    print("hello from function")
my_function()
###########################################
def my_function(fname):
    print("welcome"+fname)
my_function("jay")
my_function("parth")
my_function("dhruvin")
###########################################
def my_function(fname,lname):
    print(fname+" "+lname)
my_function("alice","even")
######################################
def my_function(contry="norway"):
    print("i am from "+contry)
my_function("sweeden")
my_function("india")
my_function()# this function will take default value
my_function("brazil")
###########################################################3
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))
