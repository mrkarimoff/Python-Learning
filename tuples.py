my_tuple = (1, 34, 2, 5, 7)
new_list = list(my_tuple)

print(my_tuple)
print(new_list)

# unpacking tuple
(var1, var2, *var3) = my_tuple

print(var1)
print(var3)
