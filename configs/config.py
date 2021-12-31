import pytz
import configs.cred as cred

time_format = '%Y-%m-%d %H:%M:%S'
suntime_format = '%H:%M:%S'
token = cred.telegram_token
owm_appid = cred.owm_appid
city_id = '524901'
db_file_path = cred.db_pth
tz=pytz.timezone("Europe/Moscow")