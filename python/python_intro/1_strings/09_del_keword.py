text = input('Enter the string: ')
print(f"Initialised string: {text}\n")

if text == 'Abhinav' or  text == "Muskan":
    del text
    text = input("Enter the string again other than abhinav: ")
    print(f"Corrected string: {text}")
