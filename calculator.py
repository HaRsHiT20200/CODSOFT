print("********* Basic calculator**********")
print("\nEnter # as operator for exit\n")
while True:
    num1=int(input("1st Value: "))
    num2=int(input("2st Value: "))
    print("Choose an operator: +  -  *  /")
    op=input()
    if op=="+":
        print(f"{num1}+{num2}=",num1+num2)
    elif op=="-":
        print(f"{num1}-{num2}=",num1-num2)
    elif op=="*":
        print(f"{num1}*{num2}=",num1*num2)
    elif op=="/":
        print(f"{num1}/{num2}=",num1/num2)
    elif op=="#":
        break
    else:
        print("Enter valid operator")
