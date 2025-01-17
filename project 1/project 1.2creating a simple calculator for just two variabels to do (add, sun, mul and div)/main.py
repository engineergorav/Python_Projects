#  creating a simple calculator for just two variabels to do (+,-,*,/)

def subtraction(a,b):
    print(f"{a} - {b} = {round(a-b,2)}.")

def addition(a,b):
    print(f"{a} + {b} = {round(a+b,2)}.")

def multipication(a,b):
    print(f"{a} X {b} = {round(a*b,2)}")

def division(a,b):
    if(b!=0):
        print(f"{a} / {b} = {round(a/b,2)}")
    else:
        print("INFINITY")
        print(f"because division by {b} is not possible: ")

while True:
    entery=(input("type E if want to proceed or type Q if want to exit:  ")).lower()
    if(entery =="e" ):
        function=input("please enter the operation want to perform (+,-,*,/): ")

        if(function!="+" and function!="-" and function!="*" and function!="/"):
            print("wrong operation entered: try again  ") 
            continue

        else:
            value_a = float(input("enter the first value: "))
            value_b = float(input("enter the second value: "))
            
            if(function=="+"):
                addition(value_a,value_b)
            elif(function=="-"):
                subtraction(value_a,value_b)
            elif(function=="*"):
                multipication(value_a,value_b)
            elif(function=="/"):
                division(value_a,value_b)
    elif(entery=="q"):
        print("EXIT done:")
        break
    else:
        print("INVALID ENTERY, TRY AGAIN:   ")
        break
