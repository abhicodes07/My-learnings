# Initialising a Dictionaries
komi = {
    'Crush' : 'komi',
    'Anime_name' : "Komi can't communicate",
    'Common' : 'Communication disorder',
    'Reason' : 'I relate and love to komi san. I am attracted to the people who are quite and always vibing in thier own world',
    'rewatch' : 'I would like to watch it again few days.'
}
print("Initialised dictionary: ",komi)
print("\n\n")
print("\t\t#### DICTIONARY ####")

for i in komi:
    print("\t",i,":",komi[i])

print("\n\n")
print("Accessing keys using key: \n",komi.keys())
print("\n\n")
print("Accessing keys using item: \n",komi.items())
print("\n\n")
print("Accessing keys using value: \n",komi.values())

