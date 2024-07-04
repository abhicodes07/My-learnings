gangsta_weather: str = 'rain'

match gangsta_weather:
    case 'rain':
        print('yo!, find yourself umbrella.')

    case 'sunny':
        print("yo! find yourself a hat")
    
    # default
    case _: # '_' is a anonymous variable 
        print("I have no idea ask bob")
