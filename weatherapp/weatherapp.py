# weatherapp.py was written by Khasan Rashidov
import pyowm

from colorama import init
from colorama import Fore, Back, Style
init()

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
mgr = owm.weather_manager()

print(Fore.BLACK)

place = 'place'
while(place != 'exit'):
    print(Back.GREEN)
    print('#' * 50)
    print(Back.CYAN)
    try:
        place = input("Enter city/country or 'exit' to exit: ")

        if (place == 'exit'):
            break
        observation = mgr.weather_at_place(place)
        w = observation.weather
        print(Back.YELLOW)
        print(place, "weather information:")
        print("Weather status:", w.detailed_status)
        print("Wind speed:", w.wind()['speed'], "m/s")
        print("Humidity:", w.humidity, "%")
        print("Temperature:", w.temperature('celsius')['temp'], "C")
        print("Feels like:", w.temperature('celsius')['feels_like'], "C")
        print("Clouds:", w.clouds, "%")
        
    
    except pyowm.commons.exceptions.NotFoundError:
        print(Back.RED)
        print('WRONG CITY OR COUNTRY NAME, TRY AGAIN!')
    
    

print(Back.GREEN)
print('#' * 50)

print(Back.WHITE)
input("Press any key to close...") 
