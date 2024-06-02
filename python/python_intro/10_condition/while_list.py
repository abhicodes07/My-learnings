# This is a program to demonstrate while loop 
# and storing values in a list

user_input = ''
inputs = []
while user_input.lower() != 'done':
    if user_input:
        inputs.append(user_input)
    user_input = input("Enter the items and press done when done: ")
print("Data: ", inputs)




