#Simple calculator
class Calulator:
def add(a, b):
    sum = a + b
    print("The sum is: ", sum)

def subtract(num_1, num_2):
    #check for bigger number
    difference = ""
    if num_1 > num_2:
        difference = num_1 - num_2
    else:
        difference = num_2 - num_1
    print("The difference is: ", difference)

def multiplication(operand_1, operand_2):
    product = operand_2 * operand_1
    print("The product is: ", product)

def divide(numerator, denominator):
    quotient = ""
    if(denominator == 0):
        print("Division using zero is not allowed")
    else:
        quotient = (numerator/denominator)
    print("Quotient is: ", quotient)


#Menus for user
user_action = ""
def menu():
    print("Welcome to simple calculator.Choose action:\n\n 1.Add \n 2.Substract \n 3.Multiplication \n 4.Division \n 5.Exit")
    user_action = int(input())

    if user_action == 5:
        print("Program exited...")
        return

    #Enter first number
    print("Enter first number: \n")
    first_number = int(input())

    # Enter second number
    print("Enter second number: \n")
    second_number = int(input())

    #Checking for action
    if user_action == 1:
        add(first_number, second_number)
    elif user_action == 2:
        subtract(first_number, second_number)
    elif user_action == 3:
        multiplication(first_number, second_number)
    elif user_action == 4:
        divide(first_number, second_number)
    elif user_action == 5:
        print("Program exited.")
    return

#Run without re-run
while user_action != 5:
    menu()

    #Exit on termination
    if user_action == 5:
        print("Exiting calculator as requested")
        break