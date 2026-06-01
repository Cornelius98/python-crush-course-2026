#Primary if statement
motion_detected = 30
heat_capacity = 50
average = (motion_detected + heat_capacity)/2

if motion_detected > average or heat_capacity > average:
    print("Intrusion detected")
else:
    print("All alerts muted")


#Chained if statement (morning, afternoon or night)
"""'
morning - please wake up
afternoon - take a break
Evening - Online classes starting
Night - Time to sleep
"""

c_input = int(input("Choose Time of Day \n 1. Morning \n 2. Afternoon \n 3. Evening \n 4. Night"))
print("\n You have chosen: ", c_input)

if c_input == 1:
    print("Please wake up")
elif c_input == 2:
    print("Take a break")
elif c_input == 3:
    print("Online classes starting")
elif c_input == 4:
    print("Time to sleep")
else:
    print("No accepted entry entered")

#Nested if statements (inner if statements)
employee_name = "royce"
password = "1234"

#checking authorization
if employee_name == "royce" and password == "1234":
    print("Authorized employee")

    #assumed bank balance
    b_balance = 10000
    average_balance = 150000
    if b_balance >= average_balance:
        print("You account is within limit")
    else:
        print("Account has insufficient balance")

else:
    print("Unauthorized employee attempt")

    # assumed bank balance
    b_balance = 10000
    average_balance = 150000
    if b_balance >= average_balance:
        print("You account is within limit")

        # assumed bank balance
        b_balance = 10000
        average_balance = 150000
        if b_balance >= average_balance:
            print("You account is within limit")
        else:
            print("Account has insufficient balance")

    else:
        print("Account has insufficient balance")
