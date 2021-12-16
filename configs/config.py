import configs.cred as cred

time_format = '%Y-%m-%d %H:%M'
token = cred.telegram_token
location = 'UUWW'
# UUWW -Код Внуково
URL_metar = 'https://tgftp.nws.noaa.gov/data/observations/metar/stations/{0}.TXT'.format(location)
owm_appid = cred.owm_appid
ya_appid = cred.yandex_appid
city_id = '524901'
