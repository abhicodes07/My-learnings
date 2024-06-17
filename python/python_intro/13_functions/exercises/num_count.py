# a program to demonstrate counting numbers to given length
# recursion can be useful here
# will append it to a list

def numadd(length: int) -> int:
    add = 0
    for i in range(1, length+1):
        add += i
    print(add)

numadd(10)




