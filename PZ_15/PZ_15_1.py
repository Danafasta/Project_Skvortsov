# Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации.
#БД должна содержать таблицу Нотариальные услуги со следующей структурой записи: ФИО клиента, услуга, сумма сделки, комиссионные(доход конторы). Программа должна обеспечивать функционал по вводу данных в БД(10 позиций), их поиску, удалению и редактированию. При организации поиска, удалении и редактировании использовать условие, предусмотреть по три SQL-запроса для каждой операции.
import sqlite3 as sq

def init_db():
    with sq.connect("notary.db") as con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS notary_services")
        cur.execute("""CREATE TABLE IF NOT EXISTS notary_services(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_fio TEXT NOT NULL,
            service TEXT NOT NULL,
            deal_sum REAL NOT NULL,
            commission REAL NOT NULL
        )""")

def insert_data():
    records = [
        ("Иванов И.И.", "Договор купли-продажи", 150000.0, 5000.0),
        ("Петров П.П.", "Свидетельство о наследстве", 80000.0, 3000.0),
        ("Сидорова С.С.", "Доверенность", 1000.0, 200.0),
        ("Козлов К.К.", "Договор дарения", 200000.0, 7000.0),
        ("Морозова М.М.", "Свидетельство о наследстве", 95000.0, 3500.0),
        ("Волков В.В.", "Договор купли-продажи", 300000.0, 10000.0),
        ("Лебедева Л.Л.", "Доверенность", 1200.0, 250.0),
        ("Новиков Н.Н.", "Договор аренды", 50000.0, 1500.0),
        ("Федорова Ф.Ф.", "Договор купли-продажи", 180000.0, 6000.0),
        ("Алексеева А.А.", "Доверенность", 1100.0, 220.0)
    ]
    with sq.connect("notary.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM notary_services")
        cur.executemany("INSERT INTO notary_services(client_fio, service, deal_sum, commission) VALUES (?, ?, ?, ?)", records)
        print("Данные успешно добавлены.")

def search_db():
    with sq.connect("notary.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM notary_services WHERE client_fio LIKE 'Иванов%'")
        print(list(map(lambda x: "ID:" + str(x[0]) + " | " + x[1] + " | " + x[2] + " | " + str(x[3]) + " | " + str(x[4]), cur.fetchall())))
        cur.execute("SELECT * FROM notary_services WHERE service = 'Доверенность'")
        print(list(map(lambda x: "ID:" + str(x[0]) + " | " + x[1] + " | " + x[2] + " | " + str(x[3]) + " | " + str(x[4]), cur.fetchall())))
        cur.execute("SELECT * FROM notary_services WHERE deal_sum BETWEEN 100000 AND 250000")
        print(list(map(lambda x: "ID:" + str(x[0]) + " | " + x[1] + " | " + x[2] + " | " + str(x[3]) + " | " + str(x[4]), cur.fetchall())))

def delete_db():
    with sq.connect("notary.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM notary_services WHERE id = 3")
        cur.execute("DELETE FROM notary_services WHERE commission < 1000")
        cur.execute("DELETE FROM notary_services WHERE service = 'Договор дарения'")
        print("Удаление выполнено.")

def edit_db():
    with sq.connect("notary.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE notary_services SET commission = commission * 1.2 WHERE deal_sum > 200000")
        cur.execute("UPDATE notary_services SET service = 'Генеральная доверенность' WHERE service LIKE '%Доверенность%'")
        cur.execute("UPDATE notary_services SET deal_sum = deal_sum + 5000 WHERE client_fio LIKE 'Петров%'")
        print("Редактирование выполнено.")

def show_all():
    with sq.connect("notary.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM notary_services")
        print(list(map(lambda r: "ID:" + str(r[0]) + " | " + r[1] + " | " + r[2] + " | " + str(r[3]) + " | " + str(r[4]), cur.fetchall())))

def main():
    init_db()
    while True:
        print("\n1. Ввод данных (10 позиций)")
        print("2. Поиск")
        print("3. Удаление")
        print("4. Редактирование")
        print("5. Просмотр всех")
        print("0. Выход")
        choice = input("Выбор: ")
        if choice == "1": insert_data()
        elif choice == "2": search_db()
        elif choice == "3": delete_db()
        elif choice == "4": edit_db()
        elif choice == "5": show_all()
        elif choice == "0": break
        else: print("Неверный выбор.")

if __name__ == "__main__":
    try:
        main()
    except sq.Error as e:
        print("Ошибка БД: " + str(e))
    except Exception as e:
        print("Ошибка: " + str(e))