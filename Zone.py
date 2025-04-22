from Weather import Weather

class Zone:
    def __init__(self, name, weather):
        self.name = name
        self.weather = weather
        weather = Weather(0, 0, 0)