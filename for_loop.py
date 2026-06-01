#For loop variations

#Using a Range function
min = 0
max = 5
for i in range (min, max):
    print(i, "Testing a for loop")


#For loop printing list items
fruits = [
    "Apple",
    "Mango",
    "Guava",
    "Pineapple"
]
for fruit_name in fruits:
    print(fruit_name)
    if(fruit_name == "Guava"):
        print("Heyie, I have found guava in list")
