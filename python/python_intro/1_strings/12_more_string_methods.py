hsplitimport string
usr = input("Enter the username and pass: ")
print(len(usr))
# print(len(pas))

if len(usr) <= 5:
    input("Enter more than 5 letters: ")
    
usr1 = ''.join(reversed(usr))
print(usr1)

usr2 = usr.count('s')
print(usr2)

usr3 = usr.capitalize()
print(usr3)
