# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = sqlite3.connect('/home/opc/temp.sqlite', check_same_thread=False)


# Создаем курсор - это специальный объект который делает запросы и получает их результаты


def ins(temp: float, temp_min: float, temp_max: float):
    cursor = conn.cursor()
    cursor.execute('insert into tempo(temperature, min, max ) values (:temp,:min, :max)',
                   {
                       'temp': temp,
                       'min': temp_min,
                       'max': temp_max})
    conn.commit()

    return 'ok'


def fetchall():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tempo')
    results = cursor.fetchall()

    return results


def get_temp():
    cursor = conn.cursor()
    cursor.execute('SELECT time,temperature FROM tempo ORDER BY id DESC LIMIT 1;')
    results = cursor.fetchone()

    return results[0:2]
