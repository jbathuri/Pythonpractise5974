'''
objectname = input('Enter a string: ')
print(objectname)

def palindrome():
    reversename = objectname[::-1]  # reverse string using slicing
    print(reversename)
    if reversename == objectname:
        print("string is palindrome")
    else:
        print("string is not palindrome")

palindrome()

'''

objectname = input('Enter a string: ')
print(objectname)

def palindrome():
    listname = list(objectname)  # convert string to list
    listname.reverse()           # reverse the list in place
    reversename = ''.join(listname)  # join list back to string
    print(reversename)
    if reversename == objectname:
        print("string is palindrome")
    else:
        print("string is not palindrome")

palindrome()

