food = []
while True:
    foods = input("Enter the food: ")
    if foods == "quit":
        break
    food.append(foods)

print(food)

# above code can also be written as this one with walrus operator
while (foods := input("Enter the food: ") != "quit"):
    food.append(foods)
