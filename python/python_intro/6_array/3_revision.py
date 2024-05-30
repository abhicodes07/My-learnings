lst = list()
print(f"Initialised string: {lst}")

for i in range(0, 10):
    lst.append(i)
print("Appended string: {}".format(lst))

for i in lst:
    i = i+1
    print(i)
    print(lst)
    lst.remove(i)
    if i==2 or i==3:
        continue
