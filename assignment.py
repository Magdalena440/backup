drinks = ["tea", "coffee", "water"]
chosen_drink = drinks[1]
print(chosen_drink)
print(len(drinks))

# 1. What does each print statement display? Explain why drinks[1] selects that drink.
# Your answer:
# first print statement: coffee because Python starts counting with 0
# second print statement: 3 because the length of drinks is 3

# 2. What are the Python types of drinks and chosen_drink?
# Your answer: drinks is a list, chosen_drink is an integer
# I can check the type with the type function
print(type(chosen_drink))
print(type(drinks))