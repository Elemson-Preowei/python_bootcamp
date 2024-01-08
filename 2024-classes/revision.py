# for a single line comment
### this is still a singleline comment

"""
# this is now a multi-line comment
where you can write a paragraph as a comment
"""

# list, tuples, dictionaries
colors = ['red', 'green', 'blue']
print(colors)

# we can iterate or loop over a list
print("-------------------------------")
for color in colors:
    print(color.upper()) # print the colors in upper case letters

# dictionaries
books = [
    {
        'title': 'Things fall apart part 1',
        'author': 'William Shakespear',
        'isbn': 236784
    },
    {
        'title': '7 laws of power',
        'author': 'Sir Elemson',
        'isbn': 876352,
        'qty': 350,
        'pages': 890,
        'other_authors': ['Redmond Wilk', 'Peter Dury']
    }
]
book1 = books[0]
print(book1['title'])
print(book1['author'])

# modifying the first dictionary in the list
books[0]['pages'] = 230
print(books[0])

# classwork
"""
# using the books list, add 2 new items representing different books
"""