names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    if name == "Sara":
        continue  # stops the current iteration and goes to the next one
    print(name)

# we can have `else` statements with `for`loops
for x in range(1, 10, 2):
    print(x)
else:
    print("It's finished")

print("=================")

# nested loops
for name in names:
    for action in actions:
        print(name + " " + action + "!")
