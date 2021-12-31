import datetime

import configs.config as config
import configs.db as db
appid = config.owm_appid
weather_emoji = {
    'Clouds':"\U00002601",
    'Clear':"\U00002600",
    'Snow':"\U0001F328",
    'Rain':"\U0001F327",
    'Drizzle':"\U00002602",
    'Thunderstorm':"\U000026C8",
    'Mist':"\U0001F32B",
    'Smoke':"\U0001F52F",
    'Haze':"\U0001F52F",
    'Dust':"\U0001F52F",
    'Fog':"\U0001F32B",
    'Sand':"\U0001F52F",
    'Ash':"\U0001F30B",
    'Squall':"\U0001F300",
    'Tornado':"\U0001F32A",

}

class OwmBasic:
    def __init__(self, json):
        
        self.weather = json['weather'][0]['main']
        if self.weather in weather_emoji:
            self.emoji = weather_emoji.get(self.weather)
        else:
            self.emoji = ''
        self.weather_info = self.emoji + json['weather'][0]['description']
        self.temp = json['main']['temp']
        # Данные в гПА, 1 гПА = 0.75 мм ртутного столба
        self.pressure = float(json['main']['pressure']) * 0.75
        self.humidity = json['main']['humidity']
        self.wind_speed = json['wind']['speed']
        
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
        self.date = datetime.datetime.fromtimestamp(
            json['dt'], tz=config.tz).strftime(config.time_format)

class OwmWeather(OwmBasic):

    def __init__(self, json):
        super().__init__(json)
        self.city = json['name']
        self.sunrise = datetime.datetime.fromtimestamp(
            json['sys']['sunrise'], tz=config.tz).strftime(config.suntime_format)
        self.sunset = datetime.datetime.fromtimestamp(
            json['sys']['sunset'],tz=config.tz).strftime(config.suntime_format)
        self.daylen = datetime.datetime.fromtimestamp(
            json['sys']['sunset']) - datetime.datetime.fromtimestamp(
            json['sys']['sunrise'])
    
    def record(self):
        db.ins(
            self.date,
            self.temp,
            self.wind_deg,
            self.wind_speed,
            self.humidity,
            self.pressure,
            self.sunrise,
            self.sunset,
            self.weather)
        return 200
