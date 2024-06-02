planet_input = ''
planets = []

while planet_input.lower() != 'done':
    if planet_input :
        planets.append(planet_input)
    planet_input = input("Enter the name of the planets and type done when done: ")

planet = 0

while planet != len(planets):
    print(planets[planet])
    planet += 1


