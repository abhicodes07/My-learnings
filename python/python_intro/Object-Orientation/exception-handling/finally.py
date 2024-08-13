try:
    f = open('file.txt', 'rb')
except Exception as e:
    print(f"This is the error that occurred: {e}")
else:
    print("Program excuted.")
finally:
    print("This will always exceute.")
