def hello():
    print("Hello user")

def pack(list1, list2, list3):
    return[list1, list2, list3]

def eat_lunch(list):
    if len(list) == 0:
        print ("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")

hello()
print(pack("movies", "video games", "eating"))
eat_lunch(["grapes", "chicken", "blueberries", "muffins", "steak"])
eat_lunch(["strawberries", "apple"])
eat_lunch(["sandwiches"])
eat_lunch([])