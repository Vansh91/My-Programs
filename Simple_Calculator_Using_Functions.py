def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def main():
    operation = input('What is the operation (+,-,/,*)?')
    if(operation != '-' and operation != '+' and operation != '/' and operation != '*'):
        print('Invalid Operation')
    else:
        var1 = int(input('Enter num1:'))
        var2 = int(input('Enter num2:'))
        if (operation == '+'):
            print(add(var1, var2))
        elif(operation == '-'):
            print(subtract(var1, var2))
        elif(operation == '/'):
            print(divide(var1, var2))
        else:
            print(multiply(var1, var2))

main()
