# Dot Notation & Chaining

# This example uses two small classes to demonstrate
# the shape of code we will later see in AI API responses.


class Forecast:

    def __init__(self, city):
        # Store the city as an attribute of the object.
        self.city = city

class Weather:

    def __init__(self):
        # An attribute stores a value.
        self.temperature = 31

        # forecast is an attribute containing a list of objects.
        self.forecast = [ Forecast("Johor Bahru"), Forecast("Kuala Lumpur") ]

    def refresh(self):
        # A method performs an action.
        print("Refreshing weather data...")


def get_weather():
    # Return a Weather object.
    return Weather()


weather = get_weather()


# An attribute gives us a value.
# No () because we are not calling anything.
print(weather.temperature)
# -> 31


# A method performs an action.
# () means we are calling the method.
weather.refresh()
# -> Refreshing weather data...


# Chained access:
# Read from left to right, one step at a time.
#
# weather.forecast[0].city
#       ↓          ↓     ↓
#   attribute    index  attribute

print(weather.forecast[0])
print(weather.forecast[0].city)
# -> Johor Bahru
