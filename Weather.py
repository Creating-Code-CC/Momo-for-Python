import requests
class Weather:
    def forcast(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + "&q=Orlando"
        response = requests.get(complete_url)
        x = response.json()
        y = x["main"]
        current_temperature = y["temp"]
        celsius = current_temperature - 273.15
        fahrenheit = celsius * (9/5) + 32
        return round(fahrenheit)