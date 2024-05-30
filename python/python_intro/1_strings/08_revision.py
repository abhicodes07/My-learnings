text = input("Enter the string: ")
print(f"Initialised string: {text}")

# updating string

text1 = 'The initialised string is ' + text + ' and is immutable.' 
print(f"Updated string: {text1}")

text2 = 'lovedbynone'
print(f"Initialised string: {text2}")
text3 = text2[:4]+'is'+text2[7:]+'otherthanmyth'
print(f"Updated string: {text3}")
