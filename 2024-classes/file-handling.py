# fp = open("modules-packages.py", "w")
# print(fp.readline())
# print(fp.readline())
# print(fp.readline())
# fp.close()
# print(fp.readline())

"""
# Assingment
using python create a file called file.txt
and add the following content
- this is the first line of the file
- this is the second line of the file
"""

with open("modules-packages.py") as fp:
    for line in fp:
        print(line)
    """
    This code works, the issue was that the file `modules-packages.py`
    had no content that was why we were not getting anything printed out
    """
