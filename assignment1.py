"""
1. create a function called first and last that returns true if 
the first letter of a string is the same as the last letter of the string 
and returns false if they are different.
"""
def first_and_last(string):
    if string[0].lower() == string[-1].lower():
        return True
    return False

print(first_and_last('Test'))


"""
2. Write a function called initial that takes a phrase 
and returns the initials of the phrase in capital letters 
for example local area network will return LAN.  
"""    
def initial(string):
    result = ''
    for x in string.split():
        result += x[0].upper()
    return result
    
print(initial('local area network'))


"""
3. Using f string, format any numeric value representing 
currency in two decimal places. Using the example above.
"""

item = "toothpaste"
amount = 750
quantity = 22
price = amount*quantity

print(f"Item: {item} - Amount: ${amount:,.2f} - Quantity: {quantity} - Price: ${price:,.2f}")


