num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
operator = input("Enter an operator: ")

if(operator == '+'):
    result = num1 + num2
    print("Addition: {} + {} = {}".format(num1, num2, result))
if(operator == '-'):
    result = num1 - num2
    print("Subtraction: {} - {} = {}".format(num1, num2, result))
if(operator == '*'):
    result = num1 * num2
    print("Product: {} * {} = {}".format(num1,num2, result))
if(operator == '/'):
    result = num1 / num2
    print("Division: {} / {} = {}".format(num1,num2, result))