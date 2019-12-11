def sum(op1, op2):
    x = op1 + op2
    return x

def sub(op1, op2):
    return op1 - op2

def mul(op1, op2):
    return op1 * op2

def div(op1, op2):
    return op1 % op2

def menu():
    print(" Menu")
    print("[1] - Add")
    print("[2] - Subtract")
    print("[3] - Multiply")
    print("[4] - Divide")


print("Thank you for using PyCalc, good Byte")

opc = ""
while(opc != "x"):
    menu()
    opc = input("Select")
    if(opc == "x"):
        break
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    if(opc == '1'):
        sum_res = sum(num1, num2)
        print("sum = " + str(sum_res))
    input("Press Enter to return")
        
    if (opc == '2'):
        sub_res = sub(num1, num2)
        print("sub = " + str(sub_res))
    input("Press Enter to return")
        
    if (opc == '3'):
        mul_res = mul(num1, num2)
        print("mul = " + str(mul_res))
    input("Press Enter to return")
       
    if (opc == '4'):
        div_res = div(num1, num2)
        print("div = " + str(div_res))
    input("Press Enter to return")