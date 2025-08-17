import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2%2!=0:
        return n1/n2
    else:
        return "Division by zero is not possible!!"

functions={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    num1=float(input("enter the first number:\n"))
    should_continue=True
    while should_continue:
        for symbol in functions:
            print(symbol)
        operation=input("Enter the choice of operation\n")
        num2=float(input("enter the second number:\n"))
        answer=functions[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")

        choice=input(f"Type y to continue calculating with {answer} , or type n to start a new calculation\n")

        if choice=="y":
            num1=answer
            print(f"Your first number is {answer}")
        else:
            should_continue=False
            print("\n"*20)
            print(art.logo)
            calculator()

calculator()










