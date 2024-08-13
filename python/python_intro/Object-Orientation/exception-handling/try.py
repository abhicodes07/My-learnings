try:
    f = open('test.txt')
except Exception as e:
    print(f"An exception occurred: {e}")
print("Program didn't terminate.")

