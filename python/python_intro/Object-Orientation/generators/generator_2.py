def count_up(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up(5)
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())





