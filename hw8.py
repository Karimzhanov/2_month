import sqlite3

connect = sqlite3.connect('car.db')
cursor = connect.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS cars_list (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    car_title TEXT NOT NULL,
                    price FLOAT DEFAULT 0.0,
                    quantity INTEGER NOT NULL DEFAULT 0
                );
               ''')
# connect.commit()

def add_car(car_title, price, quantity):
    cursor.execute('''INSERT INTO cars_list (car_title, price, quantity) VALUES (?, ?, ?)''', (car_title, price, quantity))
    connect.commit()


def delete_car(car_id):
    cursor.execute('''DELETE FROM cars_list WHERE id=?''', (car_id,))
    connect.commit()



def select_cars_cheaper_than():
    cursor.execute('''
        SELECT * FROM cars_list WHERE price < 100
    ''')
    connect.commit()
    cars = cursor.fetchall()
    for car in cars:
        print(f"Car ID: {car[0]}, Title: {car[1]}, Price: {car[2]}, Quantity: {car[3]}")


add_car("Toyota Camry", 90, 5)
add_car("Honda Civic", 700, 3)
add_car ("Bmw m-5 e60", 300000.0, 2)


print ("Cars before deletion:")
select_cars_cheaper_than()

delete_car(1)

print("\nCars after deletion:")
select_cars_cheaper_than()



connect.close()
    