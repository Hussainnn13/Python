def luhncode(number):
    x = [int(z) for z in str(number)][::-1]
    
    for y in range(1, len(x), 2):
        x[y] *= 2
        if x[y] > 9:
            x[y] -= 9

    total = sum(x)
    return total % 10 == 0

number = "4532015112830366"
print(luhncode(number))
