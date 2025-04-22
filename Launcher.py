from Zone import Zone
from Weather import Weather
import tkinter as tk

class Launcher:
    def zones(self):
        cities = [
            Zone("Madrid", Weather(30, 20, 10)),
            Zone("Barcelona", Weather(25, 15, 5)),
            Zone("Valencia", Weather(28, 18, 8)),
            Zone("Sevilla", Weather(35, 25, 15)),
            Zone("Bilbao", Weather(20, 10, 2)),
            Zone("Malaga", Weather(32, 22, 12)),
            Zone("Granada", Weather(27, 17, 7)),
            Zone("Alicante", Weather(29, 19, 9)),
        ]
        return cities

    def show_weather(self, cities):
        root = tk.Tk()
        root.title("Weather App")

        label = tk.Label(root, text="Información del clima")
        label.pack()

        for city in cities:
            city_label = tk.Label(root, text=f"{city.name}: Temp {city.weather.temperature}°C, "
                                             f"Humedad {city.weather.humidity}%, "
                                             f"Veinto {city.weather.wind_speed} km/h")
            city_label.pack()

        button = tk.Button(root, text="Cargar de nuevo", command=lambda: self.show_weather(self.zones()))
        button.pack()

        root.mainloop()

    def main(self):
        self.show_weather(self.zones())