users = ["Dave", "John", "Sara", "Botir", "Qodir", "Shoqosim", "Samir"]

empty_list: list[str] = []

users.insert(0, "Bob")
users[2:2] = ["Eddie", "Alex"]

# print(users)

del users[0]

users.sort()
# print(users)

nums = [1, 78, 42, 4, 6, 2]
# 3 ways of copying the list
nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]

print(sorted(nums, reverse=True))
