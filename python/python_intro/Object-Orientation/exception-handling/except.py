try:
    f = open('text.txt', 'r')
except Exception as e:
    print("Entered into except block.")
    print(f"Error: {e}")

print("Program didn't terminate.")

