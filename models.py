import datetime

import configs.config as config

appid = config.owm_appid


class OwmWeather:
    def __init__(self, json):
        self.weather = json['weather'][0]['description']

        self.temp = json['main']['temp']
        if json['main']['temp'] < 0:
            self.prefix = '❄️'
        else:
            self.prefix = '☀️'
        self.temp_max = json['main']['temp_max']
        self.temp_min = json['main']['temp_min']
        self.wind = json['wind']
        if 'name' in json:
            self.location = json['name']
        else:
            self.location = 'no name'
        self.timestamp = json['dt']
        self.date = datetime.datetime.fromtimestamp(json['dt']).strftime(config.time_format)

    def get_daily(self):
        daily_str = '{0} {1}:\nТекущая температура *{2:.1f}*'.format(
                self.date, self.location, self.temp)
        return daily_str

    def get_forecast(self):
        forecast_str = '{0} {2}*{1:.1f}*'.format(self.date, self.temp, self.prefix)

        return forecast_str


class YandexWeather(OwmWeather):
    def __init__(self, json):
        self.weather = json['fact']['condition']

        self.temp = json['fact']['temp']

        if self.temp < 0:
            self.prefix = '❄️'
        else:
            self.prefix = '☀️'
        self.temp_max = self.temp
        self.temp_min = self.temp
        self.wind = {
            'speed': json['fact']['wind_speed'],
            'dir': json['fact']['wind_dir']
        }
        self.location = json['geo_object']['province']['name']

        self.timestamp = json['now']
        self.date = datetime.datetime.fromtimestamp(json['now']).strftime(config.time_format)
