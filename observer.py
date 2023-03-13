"""
 la clase WeatherStation es un sujeto observable que notifica
 a sus observadores cuando la temperatura cambia mediante el
 método set_temperature(). La clase TemperatureDisplay es un
 observador que imprime la temperatura actual en la consola
 cuando recibe una notificación de cambio de temperatura
 mediante el método update(). El patrón Observador permite
 que la clase WeatherStation pueda notificar a varios
 observadores, lo que la hace altamente extensible y flexible.
"""


# Clase Observable
class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


# Clase Observador
class Observer:
    def update(self, *args, **kwargs):
        raise NotImplementedError()


# Clase de Sujeto Concreto
class WeatherStation(Observable):
    def set_temperature(self, temperature):
        self.notify_observers(temperature=temperature)


# Clase de Observador Concreto
class TemperatureDisplay(Observer):
    def update(self, *args, **kwargs):
        temperature = kwargs.get("temperature")
        print(f"La temperatura actual es: {temperature}")


# Uso del patrón Observador
weather_station = WeatherStation()
temperature_display = TemperatureDisplay()

weather_station.add_observer(temperature_display)

weather_station.set_temperature(25)
# Output: La temperatura actual es: 25

weather_station.set_temperature(27)
# Output: La temperatura actual es: 27

weather_station.remove_observer(temperature_display)

weather_station.set_temperature(30)
# No hay salida de texto, ya que el observador ha sido eliminado
