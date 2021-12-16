import datetime
from urllib import request

from metar import Metar

import configs.config as config

url_metar = config.URL_metar


def get_metar():
    try:
        ret = request.urlopen(url_metar).read().decode('utf-8')
    except Exception as e:
        print(e)
        pass
    else:
        ret = parse_data(ret)
        return ret


def parse_data(code):
    ret = code.split('\n')[1]
    return ret


def get_message():
    ret = '{0}\nТемпература воздуха: {1}'.format(get_time(), get_raw().temp)
    return ret


def get_time():
    time = get_raw().time
    now = datetime.datetime.replace(time, tzinfo=datetime.timezone.utc).astimezone(tz=None)
    ret = '{0} {1}'.format(now.date(), now.time())
    return ret.replace('-', '.')[5:-3]


def get_raw():
    return Metar.Metar(get_metar())
