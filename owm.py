import requests
import configs.config as config
import models

owm_payload = {'id': config.city_id,
               'units': 'metric',
               'lang': 'ru',
               'APPID': config.owm_appid}


def get_owm():
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/weather?",
        params=owm_payload).json()
        data = models.OwmWeather(res)
        
        msg_string = '{0} {1}\n\
        Температура: {2}°С\n\
        Ветер {3} {4} м\с\n\
        {5}'.format(data.city, data.date, data.temp, data.wind_deg, data.wind_speed, data.weather)
        return msg_string
    except Exception as e:
        print("Exception (weather):", e)
        pass

