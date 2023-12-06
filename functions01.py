def calculate(first, second, operation, make_float, message = "The result is"):
    if operation == 'add':
        result = first + second
    elif operation == 'subtract':
        result = first - second
    elif operation == 'multiply':
        result = first * second
    else:
        result = first // second
        for x in result:
            if make_float == False:
                result = int(result)
            else:
                result = float(result)

    return f"{message} {result}"
                
                
print(calculate(20, 2, operation = 'subtract', make_float = True, message = 'The result is'))