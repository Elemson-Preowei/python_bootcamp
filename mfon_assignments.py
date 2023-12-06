"""
1.
Write a program that will take a number and print out the multiplication table column for that number. 
Multipliers in the column should go from 1 to 12.
"""
def mul_table(num):
    x = 1
    while x <= 12:
        print(f'{num} x {x} = {num*x}')
        x += 1

"""
2.
Write a program that takes a number n, and prints out: one 1, two 2's, three 3's... 
and continues the pattern till n.
"""

def repeater(n):
    rep = 1
    for num in range(1,n+1):
        num = str(num)
        print(num*rep)
        rep +=1

# Mfonism says:
# This looks great. I have one tiny improvement here.
# The key is to notice that each number x is repeated x times.
# 1 is repeated 1 time
# 2, 2 times
# 3, 3 times
# So we really don't have need for the variable `rep`

def repeater_v2(n):
    for num in range(1,n+1):
        print(str(num) * num)

"""
3.
Now write a program that takes a number n, and prints out the reverse of 
what the program in number 2 above prints.
"""

def repeater_rev(n):
    rep = n
    for num in range(n,0,-1):
        num = str(num)
        print(num*rep)
        rep -=1

# You can use the strategy from `repeater_v2` to make
# this one more compact as well

"""
4.
Write a program that takes a number n and returns the sum of all the numbers from 1 to n.
For example, if the program is given the number 6, it should return 21 (which is 1 + 2 + 3 + 4 + 5 + 6).
"""

def sum_of_nos(num):
    res = 0
    for x in range (num+1):
        res += x
    print(res)

# Careful there superman!
# The instruction says to return, and not to print.
# But this looks great!!

"""
5.
Write a program that takes a number and returns its factorial. 
The factorial of a number is the product of all the numbers from 1 to that number.
For example, the factorial of 6 is 720 (which is 1 * 2 * 3 * 4 * 5 * 6).
"""

def fact_of_nos(num):
    v = 1
    fact = 1
    for x in range (1, num+1):
       fact = v * x
       v = fact
    print(fact)

# Hmmmmmmm
# This could be a lot simpler

def factorial(num):
    temp = 1
    for i in range(1, num + 1):
        temp = temp * i
    return temp

# Yeah, and also, return don't print!

"""
6.
Write a program that returns the largest number in a list of numbers.
For example, if the program takes the list [1, 4, 6, 2, 3, -9] it should return 6.
Please do not use the `max` function.
"""

def largest(list):
    list.sort()
    return list[-1]

# Oooooooh. This is smart.
# 👏🏾👏🏾👏🏾👏🏾👏🏾👏🏾👏🏾👏🏾

# That said, can you do it without sorting?
# Please do it without sorting and reach out to me.

"""
7.
Write a program that returns the smallest number in a list of numbers.
For example, if the program takes the list [13, 7, 12, 11, 6, 8] it should return 6.
Please do not use the `min` function.
"""

def smallest(list):
    list.sort()
    return list[0]

# Yep. This too. Please do it without sorting and reach out to me.

"""
8.
Write a program that returns the length of a list.
For example, if the program takes the list 
["Python", "Haskell", "Smalltalk", "Scheme", "Rust", "Elixir"] it should return 6.
Please do not use the `len` function.
"""

def length(list):
    freq = 0
    for x in list:
        freq += 1
    return freq

"""
9.
Write a program that returns the sum of the numbers in a list of numbers.
For example, if the program takes the list [1, 2, 3] it should return 6.
Please do not use the `sum` function.
"""

def list_sum(list):
    sum = 0
    for x in list:
        sum += x
    return sum

# Awesome!
# But, heads-up: `sum` is a keyword in Python.
# You don't want to use it as avariable name o!
# Bad things could happen.
# Very, very bad things could happen.

"""
10.
Write a program that checks the validity of a password.
"""  

def validity():
    v = input('Enter Password ')
    if v == 'Assignment_Completed':
        print ('Very Good!')
    else:
        print('Bad Student! Mfon will flog you!')
