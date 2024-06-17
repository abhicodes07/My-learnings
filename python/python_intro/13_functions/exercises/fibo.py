# a program to demonstrate fibonacci series

def fibo(length):
    a = 0
    b = 1

    print(a)
    print(b)
    for i in range(length):
        x = a + b
        a = b
        b = x
        print(x)

fibo(20)



