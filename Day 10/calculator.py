

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for key in operations:
            print(key)
    should_continue=True

    while should_continue:
    
        operation_symbol=input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?; "))
        function=operations[operation_symbol]
        answer=function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart.: ")=="y":
            num1=answer
        else:
            should_continue=False
            calculator()

    print(f"{num1} {operation_symbol} {num2} = {answer}")

calculator()