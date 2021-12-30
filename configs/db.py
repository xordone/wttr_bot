# CREATE TABLE temper (
#     "time" TEXT NOT NULL,
#     "temperature" REAL NOT NULL,
#     "wind_deg" TEXT NOT NULL,
#     "wind_speed" REAL NOT NULL,
#     "humidity" REAL NOT NULL,
#     "pressure" REAL NOT NULL,
#     "sunrise" TEXT NOT NULL,
#     "sunset" TEXT NOT NULL,
#     "weather" TEXT NOT NULL
# )



# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = sqlite3.connect('/home/pxl/py/bot4test/temp.sqlite', check_same_thread=False)


# Создаем курсор - это специальный объект который делает запросы и получает их результаты


def ins(
    time,
    temperature:float,
    wind_deg:str,
    wind_speed:float,
    humidity:float,
    pressure:float,
    sunrise:str,
    sunset:str,
    weather:str,
    ):
    cursor = conn.cursor()
    cursor.execute('insert into temper\
        (time, temperature, wind_deg, wind_speed, humidity, pressure, sunrise, sunset, weather )\
        values \
        (:time, :temperature, :wind_deg, :wind_speed, :humidity, :pressure, :sunrise, :sunset, :weather)',
        {
        'time' : time,
        'temperature' : temperature,
        'wind_deg' : wind_deg,
        'wind_speed' : wind_speed,
        'humidity' : humidity,
        'pressure' : pressure,
        'sunrise' : sunrise,
        'sunset' : sunset,
        'weather' : weather,
        })
    conn.commit()

    return 'ok'


def fetchall():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM temper')
    results = cursor.fetchall()

    return results



