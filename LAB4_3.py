def seperately(x):
    stack = []
    
    while x:
        smallest = min(x)
        stack.append(smallest)
        x.remove(smallest)
    
    return stack

text = "Lays, Coke, Juice, Bike"
x = text.split()
stack = seperately(x)
print(" ".join(stack))
