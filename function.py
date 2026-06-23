#Function without parameters
def sayName():
    print("Python Programming")

#function invocation
sayName()
sayName()
sayName()


#Function prototyped with parameters
def add(a, b):
    sum = a + b
    print("Sum of a ", a, "and b ", b, "is: ", sum )


""""
2,2
3,3
4,4
5,5
6,6

"""
add(2, 2)
add(3, 3)
add(4, 4)



""""
2,2
3,3
4,4
5,5
6,6

"""
a = 2
b = 2
sum = a + b
print(sum)

c = 3
d = 3
sum_c = c + d
print()


#Return statement inside a function
def printValue():
    a = 10
    b = 20
    sum = a + b
    print("Print function: ", sum)

printValue()

def returnValue():
    a = 10
    b = 20
    sum = a + b
    print("Return function: ", sum)
    return sum

isResult = returnValue()
isFinal = isResult * 10

print("Multiplied returned value: ", isFinal)
