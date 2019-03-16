def add(x,y):
    return (x+y)
def subract(x,y):
    return (x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    return(x/y)
print("select the operation.")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
choice=input("Enter the choice(1/2/3/4):")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"-",multiply(num1,num2))
if choice=='4':
    
     if num2==0:
         print ("invalid")
     else:
         print(num1,"/",num2,"-",divide(num1,num2))
else:
    print("invalid input")
