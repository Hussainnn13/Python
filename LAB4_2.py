def lab4_2(stringinput):
    punctuation = "!()-[]{};:\,<>./?@#$%^&*_~ "
    conclusion = ""

    for x in stringinput:
        if x not in punctuation:
            conclusion += x

    return conclusion

input = "Assalamualikum! My name,Hussain. It is quite good!!."
cleanedinput = lab4_2(input)
print(cleanedinput)
