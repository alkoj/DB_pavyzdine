 # # 1Isrinkite duomenis apie darbuotoja (asmens koda, varda ir pavarde) is lentelés DARBUOTOJAS
 # kurle butu gime 1988m liepos 20a.
 # - 2.Isrinkite visus duomenis apie darbuotoius
 # is lenteles DARBUOlUJAs, kurle yra gime iki 1988m
 # liepos 29d
 # - 3. Isrinkite duomenis apie darbuotojus (dirba nuo kada ir gimimo metus) is lenteles
 # DARBUOTOJAS, Kurle butu sidarbine nuo 20uym spallo sua 1k1 2012m Lapkr1C10 Ila.
 # - 4. Isrinkite duomenis apie darbuotojus (varda, Skyriu ir Projekto ID)
 # is lentelés DARBUOTOJAS
 # kurie dirba 2 ir 3 proiektuose. (Panaudoti IN operatoriu).
 # - 5. Isrinkite duomenis (varda, pavarde ir asmens koda) apie visas moteris is lentelés DARBUOTOJAS
 # (panaudojant operatoriu uKE) •
 # - 6. Isrinkite visus duomenis apie visus darbuotojus is lentelés DARBUOTOJAS, kurie yra gime 12
 # diena (panaudojant operatoriu LIKE).
 # - T.iörinkite visus projektus is lentelés PROJEKTAS kad projekto pavadinime 3 raide bütu 'u'.
import sqlite3

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