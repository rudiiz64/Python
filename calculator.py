# Basic calculator with different functions
# Add, Sub, Mult, Div, Ceiling, Floor, more too implement

# Implementations needed: Number & operand check, Integral, Snake mode

# Helper Function for Number check


def main():
    while True:
        inputx = 0
        inputy = 0
        result = 0
        restart = 0

        inputx = input("Enter a value: ")
        inputx = numCheck(inputx)
        if inputx == "kill":
            print("Invalid number!\n")
        else:
            inputy = input("Enter a second value: ")
            inputy = numCheck(inputy)
            if inputy == "kill":
                print("Invalid Number!\n")
            else:
                op = input("Enter an operand (+, -, /, *): ")
                result = opCalc(op, inputx, inputy)
                if result == "DivZero":
                    print("Cannot divide by zero!\n")
                elif result == "none":
                    print("Invalid Operand!\n")
                else:
                    print(inputx, op, inputy, '=', result, '\n')
        restart = input("Continue (y/n)? ")
        if restart == 'n' or 'N':
            break
        else:    

def numCheck(x):
    try:
        valx = int(x)
        return valx
    except ValueError:
        try:
            valx = float(x)
            return valx
        except ValueError:
            valx = "kill"
            return valx
            
def opCalc(oper, x, y):
    if oper == '+':
        return x+y
    elif oper == '-':
        return x-y
    elif oper == '/':
        if y == 0:
            return "DivZero"
        else:
            return x/y
    elif oper == '*':
        return x*y
    else:
        return "none"

main()