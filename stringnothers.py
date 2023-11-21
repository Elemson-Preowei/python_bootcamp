"""
name = "i am learning python programming language"

print(len(name))

print(name.upper())
#extracting python from name
name2 = name[-8:]
print(name2)
"""
item = "toothpaste"
amount = 750
quantity = 22
price = amount*quantity

#print("Item: " + item + ' -' + " Amount: " + '$' + str(amount) + ' -' + " Quantity: " + '$'+ str(quantity) + ' -' + " Price: " + '$' + str(price) )

print(f"Item: {item} - Amount: ${amount:,.2f} - Quantity: {quantity} - Price: ${price:,.2f}")



"""
1. create a function called first and last that returns true if the first letter of a string is the same as the last letter of a string 
and returns false if they are different
2. Write a function called initial that takes a phrase and returns the initials of the phrase in capital letters 
for example local area network will return LAN  
3. Using f string, format any numeric value representing currency in two decimal places. Using the example above.
"""