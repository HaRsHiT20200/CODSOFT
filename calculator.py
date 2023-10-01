print("********* Basic calculator**********")

print("\nEnter # as operator for exit\n")

# loop for performing unlimited operations 
while True:

    #get numbers as num1 and num2
    num1=int(input("1st Value: "))

    num2=int(input("2st Value: "))

    # get operator from user
    
    op=input("Choose an operator: +  -  *  /")

    
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
