def sayHI():                #define new func in python
    print("Hello User")
    print(" ")
sayHI()

# *******************************************************************

def say_Hi(name):              #define func with 1 parameter
    print("Hello {}".format(name))
    print(" ")

say_Hi(input("Enter a name: "))

#********************************************************************

def say_Hye(name,age):           #define func with 2 parameters
    print("Hello {}, your age are {}".format(name,age))
    print(" ")

say_Hye(input("Enter a name: "),input("Enter your age: "))

