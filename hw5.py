import sqlite3

connect = sqlite3.connect("car.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS car
             (id INTEGER PRIMARY KEY,
              number TEXT,
              brand TEXT,
              color TEXT,
              model TEXT,
              year INTEGER,
              description TEXT,
              status TEXT);""")

number = int(input("Введите номер машины: "))
brand = input("Введите бренд машины: ")
color = input("Введите цвет машины: ")
model = input("Введите модель машины: ")
year = int(input("Введите год машины: "))
description = input("Введите описание машины: ")
status = input("Введите cтатус машины: ")




def add_car(number, brand, model, color, year, description, status):
    cursor.execute(f"INSERT INTO car (number, brand, model, color,  year, description, status) VALUES ('{number}','{brand}','{model}','{color}', {year} , '{description}','{status}'  ) ")
    connect.commit()
add_car(number,brand,model, color, year, description, status)
def update_car(id, brand=None,  model=None, year=None, description=None, status=None):
    update_query = "UPDATE cars SET "
    updates = []
    if brand:
        updates.append(f"brand = '{brand}'")
    if model:
        updates.append(f"model = '{model}'")
    if year:
        updates.append(f"year = {year}")
    if description:
        updates.append(f"description = '{description}'")
    if status:
        updates.append(f"status = '{status}'")
        upupdate_query += ", ".join(updates) + f" WHERE id = {id}"
    cursor.execute(update_query)
    connect.commit()

def view_all_cars():
    cursor.execute("SELECT * FROM cars WHERE status != 'ready'")
    car = cursor.fetchall()
    return car


def close_db_connection():
    connect.close





