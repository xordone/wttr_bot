import datetime

import configs.config as config

appid = config.owm_appid


class OwmWeather:
    def __init__(self, json):
        self.weather = json['weather'][0]['main']

        self.temp = json['main']['temp']
        self.pressure = json['main']['pressure']
        self.humidity = json['main']['humidity']
        self.city = json['name']
        self.wind_speed = json['wind']['speed']
        
        self.date = datetime.datetime.fromtimestamp(json['dt']).strftime(config.time_format)
        def toTextualDescription(degree):
            if degree>337.5: return 'Северный'
            if degree>292.5: return 'Северо Западный'
            if degree>247.5: return 'Западный'
            if degree>202.5: return 'Юго Западный'
            if degree>157.5: return 'Южный'
            if degree>122.5: return 'Юго Восточный'
            if degree>67.5: return 'Восточный'
            if degree>22.5: return 'Северо Восточный'
            return 'Северный'
        self.wind_deg = toTextualDescription(json['wind']['deg'])
