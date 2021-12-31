import requests
import configs.config as config
import models

owm_payload = {'id': config.city_id,
               'units': 'metric',
               'lang': 'ru',
               'APPID': config.owm_appid}

param_list = [
    'temperature',
    'wind_deg',
    'wind_speed',
    'humidity',
    'pressure',
    'sunrise',
    'sunset',
    'weather',]

def get_weather():
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/weather?",
        params=owm_payload).json()
        data = models.OwmWeather(res)
        
        msg_string = '{0} {1}\nТемпература: {2}°С\nВлажность {6}%\nВетер {3} {4} м\с\n{5}'.format(
            data.city,
            data.date,
            data.temp,
            data.wind_deg,
            data.wind_speed,
            data.weather_info,
            data.humidity)
        return msg_string
    except Exception as e:
        print("Exception (weather):", e)
        pass
def get_etc():
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/weather?",
        params=owm_payload).json()
        data = models.OwmWeather(res)
        
        msg_string = 'Восход: {0}\nЗакат: {1}\nПродолжительность: {2}'.format(
            data.sunrise,
            data.sunset,
            data.daylen)
        return msg_string
    except Exception as e:
        print("Exception (weather):", e)
        pass


def get_class():
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/weather?",
        params=owm_payload).json()
        data = models.OwmWeather(res)
        return data
    except Exception as e:
        print("Exception (weather):", e)
        pass

def get_forecast():
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/forecast?",
        params=owm_payload).json()
        obj_list = []
        for i in res['list']:
            obj = models.OwmBasic(i)
            msg = '*{0}*\n\tТемпература: {1}°С\n\tВлажность: {3}%\n\tДавление: {2}'.format(
                obj.date,
                obj.temp,
                obj.pressure,
                obj.humidity
            )
            obj_list.append(msg)
        return '\n'.join(obj_list)
    except Exception as e:
        print("Exception (weather):", e)
        pass
