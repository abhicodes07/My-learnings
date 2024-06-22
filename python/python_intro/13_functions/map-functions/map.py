
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

numbers = [x for x in range(1, 10)]

fact_num = map(factorial, numbers)
facted_num = list(fact_num)

print(facted_num)


