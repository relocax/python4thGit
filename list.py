fruits = ["apple", "mango", "banana", "orange", "cocunut"]
# print(fruits[::3])
# print(len(fruits))
# print("apple" in fruits)
# print(dir(fruits))
# print(help(fruits))

# fruits[1] = "pineapple"
fruits.append("pineapple")
for fruit in fruits:
    print(fruit)

# fruits.remove("apple")
# fruits.remove("pineapple")
fruits.sort()
fruits.reverse()
# fruits.clear()
fruits.insert(0, "pineapple")
print(fruits.index("apple")) 
print(fruits)
# extend no bracket 
# insert bracket
