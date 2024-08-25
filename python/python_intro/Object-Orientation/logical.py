def logical(x):
    if x == 1:
        print(f"Value: {x}")
        return 1
    else:
        print(f"value: {x}")
        return (x + logical(x - 1))

result = logical(3)
print(result)
