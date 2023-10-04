import random
import string

print("****** Password Generator ******")

s = ""
s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = "!@#$%&*_?"

loop=True
while loop:
    print("\nChoose difficulty level")
    print("1: Easy")
    print("2: Moderate")
    print("3: Hard")

    level = int(input("Level:  "))
    if level==1:
        s = s1 + s2
        length = int(input("Enter length of password: "))
        if length==0:
            break
        password = "".join(random.sample(s,length))
        print(f"Your password is: {password}")  


    elif level==2:
        s = s1 + s2 + s3
        length = int(input("Enter length of password"))
        if length==0:
            break
        password = "".join(random.sample(s,length))
        print(f"Your password is: {password}")  

    elif level==3:
        s = s1 + s2 + s3 + s4
        length = int(input("Enter length of password"))
        if length==0:
            break
        password = "".join(random.sample(s,length))
        print(f"Your password is: {password}")

    else:
        print("Level not found. Try again")
      







