#Match statement - simplify chained if statement
day = 1
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case _:
        print("No value found")

if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tueday")
else:
    print("No value found")