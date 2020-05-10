str = 'X-DSPAM-Confidence: 0.8475 '

pos = str.find(':')
numb = float(str[pos+1:])
pos2 = str.find('0')
numb2 = float(str[pos2:])
print(numb, type(numb))
print(numb2, type(numb2))

# String documentation https://docs.python.org/3.5/library/stdtypes.html#string-methods
print(str.replace('e','a'))
print(str.strip('X5-'))
#str.strip('X-')

str = 'abcdefghijka almnopqrsta auvwxyza\t\t\tñññ'
str2 = 'abcdefghijka {} almnopqrsta auvwxyza  {}   ñññ'
print(str.capitalize())
print(str.casefold()) # Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. For example, the German lowercase letter 'ß' is equivalent to "ss". Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss".
print(str.center(len(str)+10))
print(str.center(-10))
print(str.count('a'))
print(str.encode())
print(str.endswith('a'))
print(str.endswith('ñ'))
print(str.expandtabs(1)) # The expandtabs() method returns a copy of string with all tab characters '\t' replaced with whitespace characters until the next multiple of tabsize parameter.
print(str.find('u'))
print(str.find('9'))
print('cde' in str) # Same as above but resolving to true or false
print(str2.format('Test1','Test2')) # https://www.geeksforgeeks.org/python-format-function/

# format_map() function is an inbuilt function in Python, which is used to return an dictionary key’s value. a variable in which input dictionary is stored and string is the key of the input dictionary.
# input stored in variable a.
a = {'x':'John', 'y':'Wick'}
# Use of format_map() function
print("{x}'s last name is {y}".format_map(a))

# print(str.find('1')) # This would return -1 not break
# print(str.index('1')) # This would break because 1 is not found in the string so it crashes

print(str.isalnum()) # A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric()

print(str.isalnum()) # Alphabetic characters are those characters defined in the Unicode character database as “Letter”
print(str.isdecimal()) # Decimal characters are those that can be used to form numbers in base 10, e.g. U+0660
print(str.isdigit()) # Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.
print(str.isidentifier()) #  test for reserved identifiers such as def and class.

print(str.islower()) # True if all chars are lowercase
print(str.isupper()) # True if all chars are uppercase

print(str.isnumeric()) #  Formally, numeric characters are those with the property value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric
print(str.isprintable())
print(str2.isprintable())

print(str2.isspace()) # Return true if there are only whitespace characters in the string and there is at least one character, false otherwise.

print(str.istitle())

print(str.join(str2)) # The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator.S
