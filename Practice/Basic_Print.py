"""
Common use of [print] function
Authored by Kai Wang.
2019-09-24
"""

# common use to print string
a, b, st = 1, 2, "johnny hassewer"
print(st)  # output entire string
print(st[0])  # output the 1st character of the string
print(st[-1])  # output the last character of the string
print(st[2:5])  # output from the 3rd character to the [5th] character of the string
print(st[2:])  # output from the 3rd character to the last character of the string
print(st * 2)  # output the string twice with on blanks in them
print(st + "TEST")  # output the string with another string attached to its ending

# common use to print integer
x = 1
k = 2
print(x)  # change line
print(k)  # change line
print("value of x is {0}; value of k is {1}".format(x, k))
print(x, k)  # do not change line
print(x,)  # change line
print(k,)  # change line

# for loop sentences
for y in range(0, 1):
    print("value of x is {0}; value of y is {1}; value of x+y is {2}".format(x, y, x+y))

# if conditional sentences
if x == 1:
    print(x)
elif x == 0:
    print("error")
else:
    print("do nothing")
