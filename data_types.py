#Data types file

#Integer data type  1001 101 10011 111
num_1 = 10
print(num_1)

#Float and double data types
float_num = 3.142
print(float_num)

#Character
char_1 = 'A'
print(char_1)

#String
name = 'Guido Van Rossum'
print(name)

#List (or Array)
fruits = ["apple", "guava", "mango"]
print(fruits)

height = [1.5, 1.2, 1, 0.98, 2.5]
print(height)

#dictionary (Hash maps) key-value
founder = {
    "name": "Guido Van Rossum",
    "age": 10,
    "country": "Netherlands"
}

print(founder)

#Tuple
my_tuple = (10, 20, 30, 50)
print(my_tuple)
print(my_tuple[2])

#List 2
fruits_2 = ["apple", "mango"]
print(fruits_2)
fruits_2.append("Guava")
fruits.append("Lemon")
print(fruits)


#Set
isSet = {10, 20, 30, 40, 50}
print(isSet)
isSet.add(100)
isSet.add(200)
print(isSet)

#List 3
fruits_3 = ["apple", "mango", "banana"]
print(fruits_3)
fruits_3.append("Guava")
fruits_3.append("Lemon")
print(fruits_3)

#remove apple
fruits_3.remove("apple")
print(fruits_3)

#update mango to "New Fruit"
fruits_3[0] = "New Fruit"
print(fruits_3)

#Byte data type
byte = b"Hellow World"
print(byte)
print(byte[0])

#byte array
byte_array = bytearray(byte)
print(byte_array[3])

#Memory view
memo_view = memoryview(byte)
print(memo_view)

#Tuple data type
coords_tuple = (10, 20, 30)
print(coords_tuple)


#printing single value
print(coords_tuple[0])
print(coords_tuple[1])

#Work around to add, update and remove from a tuple
mutable_tuple = (10, 20, 30)
print(mutable_tuple)

list_mutable_tuple = list(mutable_tuple)
print(list_mutable_tuple)

#add operation
list_mutable_tuple.append(100)
print(list_mutable_tuple)












