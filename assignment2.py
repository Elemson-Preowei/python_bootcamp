
"""
1. write a function that tries an operation. If the operation succeeds, the program stops, if it fails
the program retries for a given number of times before it stops.


def runner(operation, retries):
    res = operation()
    if res:
        return True
    
    for x in range(retries):
        print(f"Now retrying - attempt{x}")
        res = operation()
        if res:
            return True
        
    return False

"""

"""
2. Write a program that converts a binary (base 2) number to decimal (base 10). Your program should begin 
by reading the binary number from the user as a string. Then it should compute the equivalent 
decimal number by processing each digit in thebinary number. 
Finally, your program should display the equivalent decimal number with an appropriate message.
"""
"""
def base_conversion(e):
    solution = 0
    v = 0
    for x in range(len(e)-1,-1,-1):
        solution += int(e[v]) * 2**x
        v += 1
    return solution 
                   
def run_base_conversion():
    binary_string = input('Enter Binary String: ')
    result = base_conversion(binary_string)
    print(f'The result of converting {binary_string} to base 10 is {result}')

#start a while loop
#get the remainder 
#use the remainder to find the corresponding value in hexadecimal
#restate the argument
#add the last remainder to result variable
#reverse a digit of the result variable
#return a result variable

def base_conversion2(b10):
    hexa_def = "0123456789ABCDEF"
    result = " "
    remainder = 0
    b10 = b10
    while b10/16 > 0:
     remainder = b10 % 16
     v = dexa_def[remainder]
     result += str(b10/16)
"""
def base_16(base_10):
    base_16 = ''
    hex_num = '0123456789ABCDEF'

    base_10 = int(base_10)
    while base_10//16 > 0:
        rem = base_10 % 16
        base_16 += hex_num[rem]
        base_10 = base_10//16
    base_16 += hex_num[base_10]
    base_16 = base_16[::-1]
    return base_16

print(base_16(2020776))
   




