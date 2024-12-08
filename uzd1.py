import sqlite3
import csv
def select_command(komanda):
    conn = sqlite3.connect('Pavyzdine.db')
    c = conn.cursor()
    c.execute(komanda)
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

def select_employees_by_birthdate():
    query = """SELECT ASMENSKODAS, VARDAS, PAVARDE 
               FROM DARBUOTOJAS 
               WHERE GIMIMOMETAI = '1988-07-20';"""
    select_command(query)

def select_employees_born_iki_1988():
    query = """SELECT * 
               FROM DARBUOTOJAS 
               WHERE GIMIMOMETAI < '1988-07-29';"""
    select_command(query)

def select_employees_hired_between_dates():
    query = """SELECT DIRBANUO, GIMIMOMETAI, VARDAS 
                   FROM DARBUOTOJAS 
                   WHERE DIRBANUO BETWEEN '2009-10-30' AND '2012-11-11';"""
    select_command(query)


if __name__ == '__main__':
    print("Duomenys apie darbuotojus, gimusiu 1988-07-20:")
    select_employees_by_birthdate()

    print("\nVisi darbuotojai, gime iki 1988-07-29:")
    select_employees_born_iki_1988()
    print("Duomenys apie darbuotojus, isidarbinusius nuo 2009-10-30 iki 2012-11-11:")
    select_employees_hired_between_dates()

    print("Darbuotojai, kurie dirba 2 ir 3 proiektuose:")
    select_command("""SELECT vardas, projektas_id
                         FROM DARBUOTOJAS
                         WHERE projektas_id IN (2, 3);""")
    if __name__ == '__main__':
        print("Visų moterų duomenys:")
        select_command("""SELECT *
                              FROM DARBUOTOJAS
                              WHERE ASMENSKODAS LIKE '4%';""")



        print("Darbuotojų vardai ir GIMIMOMETAI, gimę 12 dieną:")
        select_command("""SELECT vardas, strftime('%Y', GIMIMOMETAI) AS GIMIMOMETAI
                              FROM DARBUOTOJAS
                              WHERE GIMIMOMETAI LIKE '%-12';""")
        print("Visi projektai, kurių pavadinime trečioji raidė yra 'u':")
        select_command("""SELECT *
                             FROM PROJEKTAS
                             WHERE pavadinimas LIKE '__u%';""")

        # Подключение к базе данных
        connection = sqlite3.connect('Pavyzdine.db')
        cursor = connection.cursor()

        # Получение данных из таблицы (замените 'ваша_таблица' на фактическое имя таблицы)
        cursor.execute("SELECT * FROM DARBUOTOJAS")
        data = cursor.fetchall()

         # Создание CSV файла
        with open('select.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Запись заголовков (проверьте, чтобы названия соответствовали колонкам в таблице)
            writer.writerow(
                ['ASMENSKODAS', 'VARDAS', 'PAVARDE', 'DIRBANUO', 'GIMIMOMETAI', 'PAREJGOS', 'SKYRIUS_PAVADINIMAS',
                 'PROJEKTAS_ID', 'DEPARTAMENTAS_ID', 'ATLYGINIMAS'])

            # Запись данных
            writer.writerows(data)

        # Закрытие соединения
        connection.close()
        print()

