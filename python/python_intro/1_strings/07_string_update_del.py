name = input("Enter your wrong name: ")
print(f"Wrong name: {name}")

# Strings are immutable in python but can 
# updated using join method 
# There are two methods for updating strings

# 1
ryt_name = list(name)
ryt_name[0:2] = 'Ab'
str_ryt_name = ''.join(ryt_name)
print(f"Updated string: {str_ryt_name}")

#2
string2 = 'I ' + 'Am ' + str_ryt_name[:] + ' asthana.'
print(string2)
string3 = string2[:4] + ' the' + string2[4:]
print(string3)
