#Assignment operator (=)
operand_1 = 100
print("Assignment operator in use", operand_1)

#increment operator (++) - increments values by one
toBeIncrementedBy1 = 0
print("toBeIncrementedBy1:", toBeIncrementedBy1)
#toBeIncrementedBy1++ #post pending ++ operator
##prepending ++ operator
toBeIncrementedBy1 = toBeIncrementedBy1 + 1
print("Incremented", toBeIncrementedBy1)

#Plus or equal to (++, --, +=, -=, /=, %=)
sumByFive = 10
sumByFive = sumByFive + 5
print("Sum By 5:", sumByFive)

sumBy20 = 30
sumBy20 = sumBy20 + 20
print("sum by 20 old notation: ", sumBy20)

#sumBy20 already has a value of 50
sumBy20 = 30
sumBy20 +=20
print("sum by 20 new notation: ", sumBy20)



a = 10
a = a + 5
print("Old notation: ", a)

b = 10
b+=5
print("New increment notation: ", b)

#Minus or equal to (-=)
minus_or_equal = 20
minus_or_equal = minus_or_equal - 10
print("Minus old notation: ", minus_or_equal)

minus_or_equal = 20
minus_or_equal -= 10
print("Minus new notation: ", minus_or_equal)

#Multiplication or equal to operator (*=)
multiply_or_equal = 30
multiply_or_equal*=100
print("*=:", multiply_or_equal)

#Divide or equal to
d_equal_to = 50
d_equal_to /=2
print("/=:", d_equal_to)
