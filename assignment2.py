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
def base_conversion(binary):
    solution = 0
    e = str(binary)
    v = 0
    for x in range(len(e)-1,0,-1):
        solution += int(e[v]) * 2**x
        v +=1
    return solution 
                   

print(base_conversion(1110011))
    
