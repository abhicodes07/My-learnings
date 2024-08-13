table = []
num = int(input("Enter the number: "))
# for i in range(10):
#     table = num * i
#
total = 0

while (mul := num * total) <= num*10:
    total += 1
    table.append(mul)

print(table)
