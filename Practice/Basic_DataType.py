"""
Common use of [data type]
Authored by Kai Wang.
2020-04-19
"""

"""
Built-in Data Types
Python has the following data types built-in by default, in these categories:
- Text Type:	    str
- Numeric Types:	int, float, complex
- Sequence Types:	list, tuple, range
- Mapping Type:	    dict
- Set Types:	    set, frozenset
- Boolean Type:	    bool
- Binary Types:	    bytes, bytearray, memoryview
"""
# - Text Type:	str
x = "Hello World"  # str

# - Numeric Types:	int, float, complex
x = 20  # int
x = 20.5  # float
x = 1j  # complex

# - Sequence Types:	list, tuple, range
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range

# - Mapping Type:	dict
x = {"name": "John", "age": 36}  # dict

# - Set Types:	set, frozenset
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset

# - Boolean Type:	bool
x = True  # bool

# - Binary Types:	bytes, bytearray, memoryview
x = b"Hello"  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memoryview

"""
Getting the Data Type
You can get the data type of any object by using the type() function:
"""
x = 5
print(type(x))

"""
Specify a Variable Type
int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
x = int(1)    # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

x = float(1)      # x will be 1.0
y = float(2.8)    # y will be 2.8
z = float("3")    # z will be 3.0
w = float("4.2")  # w will be 4.2

x = str("s1")  # x will be 's1'
y = str(2)     # y will be '2'
z = str(3.0)   # z will be '3.0'

"""
There are four collection data types in the Python programming language:
--List is a collection which is ordered and [changeable]. Allows duplicate members.
--Tuple is a collection which is ordered and [unchangeable]. Allows duplicate members.
--Set is a collection which is unordered and unindexed. No duplicate members.
--Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""
# - List is a collection which is ordered and [changeable]. Allows duplicate members.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
thislist.append("orange")
thislist.remove("banana")
thislist.pop()   # The pop() method removes the last item if index is not specified
thislist.pop(1)  # The pop() method removes the specified index
thislist.reverse()
thislist.sort()
print("orange appears " + str(thislist.count("apple")) + " times")
# del thislist[0]  # The del keyword removes the specified index
# del thislist
# thislist.clear()
mylist = thislist.copy()
mylist = list(thislist)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
list1.extend(list2)    # Use the extend() method to add list2 at the end of list1

# - Tuple is a collection which is ordered and [unchangeable]. Allows duplicate members.
x = ("apple", "banana", "cherry")
y = list(x)  # Convert the tuple into a list to be able to change it
y[1] = "kiwi"
x = tuple(y)
print(x)
# cannot add/remove any item
print("apple appears " + str(x.count("apple")) + " times")
# One item tuple, remember the commma
thistuple = ("apple",)
print(type(thistuple))
# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# - Set is a collection which is unordered and unindexed. No duplicate members.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")                          # Add an item to a set, using the add() method
thisset.update(["orange", "mango", "grapes"])  # Add multiple items to a set, using the update() method
thisset.remove("banana")                       # If the item to remove does not exist, remove() will raise an error
thisset.discard("banana")                      # If the item to remove does not exist, discard() will NOT raise an error
x = thisset.pop()                              # Remove the last item by using the pop() method
print(len(thisset))
# del thislist
# thislist.clear()

