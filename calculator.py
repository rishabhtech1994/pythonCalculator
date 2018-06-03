import re

print("Python Calculator")
print("enter quit to exit the program")
lastValue = 0
run = True


def runCalculator():
    global run
    global lastValue


    if lastValue == 0:
        input_user = input("Enter the value")
    else:
        input_user = eval(str(lastValue))

    if input_user == 'quit':
        run = False
    else:
        # using regix to remove the strings and special characters
        input_user = re.sub('[a-zA-Z,.:()" "]', '',input_user)
        if lastValue == 0:
            lastValue = eval(input_user)
        else:
            lastValue = eval(str(lastValue) + input_user)
            # print(lastValue)


while run:
    runCalculator()