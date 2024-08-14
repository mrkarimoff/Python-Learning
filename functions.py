# kwargs used to catch dynamic parameters an is in `dict` type
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Mirfayz", second="Karimov")
