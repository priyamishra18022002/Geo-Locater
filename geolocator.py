#Made by Dhiransh.py on Instagram

from colored import stylize, fg
from geopy.geocoders import Nominatim

print(stylize("\n---- | Geographuc Conversion | ----\n", fg("red")))

class GeographicConversion:
    def __init__(self, choice, locator):
        self.choice = choice
        self.locator = locator

    def convert_into_address(self, locator):
        coordinates = input("Coordinates Seperated with Comma: ")
        try:
            location = locator.reverse(coordinates)
            return stylize(str(location.address) + "\n", fg("red"))
        except:
            exit("\nInvalid Coordinates\n")

    def convert_into_coordinates(self, locator):
        address = input("Address: ")
        try:
            location = locator.geocode(address)
            return stylize(str(location.latitude, location.longitude) + "\n", fg("red"))
        except:
            exit("\nInvalid Address\n")


    def __repr__(self):
        if self.choice == "a":
            return self.convert_into_address(self.locator)
        else:
            return self.convert_into_coordinates(self.locator)

if __name__ == "__main__":
    # user interaction
    email = input("Your email address: ")
    print(stylize("\nOptions:", fg("green")))
    choice = input("'a' for coordinates into address\n\
'b' for address into coordinates\n\n: ").lower()

    # locator
    geolocator = Nominatim(user_agent=email)

    if choice != "a" and choice != "b":
        exit("\nInvalid Input\n")

    print(GeographicConversion(choice, geolocator))

