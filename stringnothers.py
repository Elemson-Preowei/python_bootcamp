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

print(f"Item: {item} - Amount: ${amount} - Quantity: {quantity} - Price: ${price}")