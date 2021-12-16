import requests

import configs.config as config
import configs.db as db
import models
import datetime

owm_payload = {'id': config.city_id,
               'units': 'metric',
               'lang': 'ru',
               'APPID': config.owm_appid}

ya_payload = {
    'lat': '55.46534',
    'lon': '36.93482',
    'lang': 'ru_RU',
}
ya_header = {
    'X-Yandex-API-Key': config.ya_appid,
    'user-agent': 'my-app/0.0.1'
}


def get_owm():
    try:
        res = requests.get("https://api.weather.yandex.ru/v2/forecast",
                           headers=ya_header, params=ya_payload).json()
        data = models.YandexWeather(res)
        return data
    except Exception as e:
        print("Exception (weather):", e)
        pass


def get_daily():
    try:
        res = requests.get("https://api.weather.yandex.ru/v2/forecast",
                           headers=ya_header, params=ya_payload).json()
        data = models.YandexWeather(res)
        return data.get_daily()
    except Exception as e:
        print("Exception (weather):", e)
        pass


def get_hourly():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params=owm_payload).json()
        ret = []
        for i in res['list']:
            ret.append(models.OwmWeather(i).get_forecast())
        return '\n'.join(ret)

    except Exception as e:
        print("Exception (weather):", e)
        pass


def get_temp():
    data = db.get_temp()
    return '{0}:\nТекущая температура *{1:.1f}*'.format(
            data[0][0:16], data[1])
