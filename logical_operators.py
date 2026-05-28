""""
AND (&& - ampersand)
requires all conditions to be true to give a true
"""
a = 10
b = 30
c = 30

if a < b and b == c:
    print("All conditions are true")
else:
    print("One condition is not true")


""""
OR (|| - Pipes)
requires one conditions to be true to give a true
"""
a = 10
b = 30
c = 30

if a >= b or b < c:
    print("One condition is true")
else:
    print("One condition is not true")

#NOT operator (! -accepted in python, <> denied)
x = 10
y = 50
if x!=y:
    print("Yes is not equal to y")
else:
    print("No is equal to y")