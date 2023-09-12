def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("welcome to the calculator!")
while True:
    print("select an operation:")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choice=int(input("enter your choice:"))
    if choice==5:
        print("Goodbye!")
        break
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    if choice==1:
        result=add(num1,num2)
        print("the result is:",result)
    elif choice==2:
        result=subtract(num1,num2)
        print("the result is:",result)
    elif choice==3:
        result=multiply(num1,num2)
        print("the result is:",result)
    elif choice==4:
        result=divide(num1,num2)
        print("the result is:",result)
    else:
        print("invalid choice.please try again.")
