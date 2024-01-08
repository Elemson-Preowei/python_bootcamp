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
    },
    {
        'title': 'Classwork of Elemson',
        'author': 'Mr Otuekong'
    },
    {
        'title': 'Chronicles of Python',
        'author': 'Mfonism'
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
# write a code to add isbn number and number of pages to the two new items
"""
books[2]['isbn'] = 200494
books[2]['pages'] = 12
books[3]['isbn'] = 200594
books[3]['pages'] = 5000

print(books)