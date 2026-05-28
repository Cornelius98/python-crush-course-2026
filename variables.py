#Integer variable
student_grade = 56
print(student_grade)

studentGrade = 87
print(studentGrade)

#Numbers in variables names
student_2 = 10
student2 = 10
_student_2 = 10
_10_student_2 = 10

#strongly typed variables
#int age = 10

#Variable Local Scope
def testScope():
    localScope = 20
    print("Locally scoped variable", localScope)

testScope()
#print(localScope)

#Variable Global Scope
globalScopedVariable = 100
print(globalScopedVariable)

def testGlobalScope():
    global globalScopedVariable
    print("Global printed in local scope", globalScopedVariable)

testGlobalScope()
print("Global variable in Global Scope", globalScopedVariable)

def add():
    x = 10
    y = 20
    z = x + y
    print("Sum", z)

add()