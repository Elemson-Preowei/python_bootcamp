#write a loop that will print numbers that are powers of 2 from 1 to 50
"""
x = 0
while x <= 50:
    if x % 2 == 0:
        print(True)
    else:
        print(False)
    x+=1
"""

#write a program that prints a number each time it loops for a certain given number 
"""
def random_number():
    x = 0
    v = int((input('What is your number?')))
    while x <= v:
        print(x)
        x+=1
    return
print(random_number()) 
"""
"""
write a function that tries an operation. If the operation succeeds, the program stops, if it fails
the program retries for a given number of times before it stops 
Write a program that converts a binary (base 2) number to decimal (base 10). Your program should begin 
by reading the binary number from the user as a string. Then it should compute the equivalent 
decimal number by processing each digit in thebinary number. 
Finally, your program should display the equivalent decimal number with an appropriate message.

"""

def pass_fail(x,y=4):
    trial = 0
    while trial <= y:



