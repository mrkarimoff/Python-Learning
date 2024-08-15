def add_one(num: int) -> int:
    if num >= 9:
        return num
    else:
        print(num)
        return add_one(num + 1)


result = add_one(1)
print("Result:", result)
