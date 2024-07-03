import time 
import math

def calculate_time(func):
    def cal(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time taken in execution: {func.__name__} = {end - begin}")
    return cal

# above code in be added to any function for calulating its execution 22:12
# here in this case factorial

@calculate_time
def factorial(num):
    time.sleep(2)
    print(f"Factorial: {math.factorial(num)}")

factorial(10)



