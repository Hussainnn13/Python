def dynamiccalculator():
    symbol = input("Enter operation (+, -, *, /): ")
    x= float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    
    if symbol == '+':
        result = x + y
    elif symbol == '-':
        result = x - y
    elif symbol == '*':
        result = x * y
    elif symbol == '/':
        result = x / y
    else:
        return "Invalid symbol of opertaion was entered. Please try again"
    
    return f"Result: {result}"

print(dynamiccalculator())
