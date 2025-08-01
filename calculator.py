logo='''           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              
                                              
'''
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations= {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    print(logo)
    should_continue=True
    x=float(input("enter first number: "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("enter a symbol: ")
        y=float(input("enter the second number: "))
        result=(operations[operation_symbol](x,y))
        print(f"{x} {operation_symbol} {y} = {result}")
        
        choice=input(f"press 'y' to continue calculation with {result} or press 'n' to continue with new number: ")
        if choice=="y":
            x=result
        else:
            should_continue=False
            print("\n"*20)
            calculator()
calculator()
 