# Sets

nums = {1, 2, 3, 4, 5}
nums2 = set((1, 2, 3, 4, 5, 6))

print(nums2)
print(type(nums2))
print(len(nums2))

# No duplicates in a set
nums = {1, 2, 4, 1}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}

# merge to sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mergedset = one.union(two)

print(mergedset)
