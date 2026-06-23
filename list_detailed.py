#Creating a list (array, collection)
import http

my_list = [] #built empty list
populated_list = [1, 2, 3, 4]

#Adding items to a list
unpopulate_list = []
print("Before populating", unpopulate_list)

unpopulate_list.append(100)
unpopulate_list.append(200)
unpopulate_list.append(300)
# unpopulate_list.append([10, 40, 50])
print(unpopulate_list)
print("After populating", unpopulate_list)

#Update items
unpopulate_list[2] = 500
print("After updating", unpopulate_list)

#Accessing items
index_0 = unpopulate_list[0]
index_1 = unpopulate_list[1]
index_2 = unpopulate_list[2]
print("Accessing 0 index:", index_0)
print("Accessing 1 index:", index_1)
print("Accessing 2 index:", index_2)

#Remove items from list
unpopulate_list.remove(500)
print("Removing Item:", unpopulate_list)

#Delete all items from list
unpopulate_list.clear()
print("Cleared List: ", unpopulate_list)


#Send request to API
result = http.get("www.research.com/consumer_behavior_in_zambia")
data = [
    ["informa about users"],
    ["informa about users"],
    ["informa about users"],
    ["informa about users"],
]

#
