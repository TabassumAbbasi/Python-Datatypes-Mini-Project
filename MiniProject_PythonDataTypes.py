# Mini Project: Python Data Types Demo

# Integer datatype
a = 5
print("Integer datatype:", type(a), float(a), bool(a), str(a), '\n\n')

# Float datatype
a = 5.0
print("Float datatype:", type(a), int(a), bool(a), str(a), '\n\n')

# Complex datatype
c = 5 + 6j
print("Complex datatype:", type(c), c, str(c), bool(c), '\n\n')

# Boolean datatype
b = True
print("Boolean datatype:", type(b), b, str(b), int(b), float(b), '\n\n')

# String datatype
s = "messageorprompt"
print("String datatype:", type(s), s, bool(s))

s2 = """
MULTI
LINES
"""
print(s2, '\n\n')

# Different functionalities on string datatype
print("String functionalities:")
print(s.upper())
print(s2.lower())
print(s[::-1])
print(s.split(), '\n\n')

# Lists
l1 = [1, 3, 5, 7, 5, 9]
l2 = [2, 4, 6, 8]
print("List datatype:", type(l1), l1)

# Different functionalities on list datatype
print("List functionalities:")
print(l1.append(11), l1)  # insert elements at the end of the list
print(l1.insert(2, 12), l1)  # insert elements in lists at specific points
print(l1.extend(l2), l1)  # add list into a new and existing list
print(sorted(l1))  # for sorting the list variable is passed in a function
print(l1.sort(), l1)  # sorted and then show the list
print(l1.reverse(), l1)  # for reversing the list
print(l1.pop(2), l1)  # for popping or removing an element from specific index
print(l1.remove(5), l1)  # directly remove elements from list
print(len(l2), l2)  # for finding the length of the list
print(l2.index(8))  # to find the element on specific index position.
print(l2[1])
print(l1.clear(), l1, '\n\n')  # clear all the list / empty the list

# Tuple
t1 = (20, 30, 30, 40, 'st', 6.5)
print("Tuple datatype:", type(t1), t1)

# Different functionalities on tuple datatype
print("Tuple functionalities:")
print(t1.count(30))  # to count the element how much appears in a tuple
print(t1.index(40))
print(t1[5])
print(100 in t1, '\n\n')

# Range
r = range(5)
print("Range datatype:", type(r), r)
print(list(r))
print(list(range(0, 100, 10)))
for i in range(0, 100, 20):
    print(i)
print('\n\n')

# Mapping data type: Dictionaries
team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])
del team['Minnesota']  # delete a particular key and value from dictionary
team['Seattle'] = 'best'  # updating the value for the key
team['pakistan'] = 'islamabad'  # adding new key and values in dictionary
print("Dictionary datatype:", type(team), team['Colorado'], team)

# 2 ways of creating dictionary
teams = dict(
    Colorado='Rockies',
    Boston='Red Sox'
)
print(teams)

# 3 ways of creating dictionary
teamss = {}
teamss[11] = 'Baber'
teamss[1] = 'Shahzad'
print(teamss)
print(teamss[11])

ascii = b'hello'  # b in this string dedicated to byte
print("Byte datatype:", type(ascii))
print(ascii)
print("Bytearray datatype:", type(bytearray(ascii)))
decode = ascii.decode('utf-8')
print(decode)
