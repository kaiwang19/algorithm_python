"""
Common use of [operator]
Authored by Kai Wang.
2020-04-19
"""

x, y = 8, 3

# **	Exponentiation
print(x ** y)  # 512
# //	Floor division
print(x // y)  # 2

# and 	Returns True if both statements are true
print(x < 5 and x < 10)       # False
print(x < 5 & x < 10)         # False
# or	Returns True if one of the statements is true
print(x < 5 or x < 4)         # False
print(x < 5 | x < 10)         # False
# xor	Returns True if only one of the statements is true
print(x < 5 ^ x < 10)         # False
# not	Reverse the result, returns False if the result is true
print(not(x < 5 and x < 10))  # True
print(~(x < 5 & x < 10))      # -1
# Zero fill left shift
print(x << 2)                 # 32 = 8 * (2 ** 2)
# Zero fill right shift
print(x >> 2)                 # 2 = 8 / (2 ** 2)
