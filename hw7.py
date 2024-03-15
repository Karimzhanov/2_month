import random
import sqlite3

connect = sqlite3.connect('user.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS clients (
               id INTEGER PRIMARY KEY,
               name VARCHAR(255),
               surname VARCHAR(255),
               age INTEGER,
               email VARCHAR(255),
               password VARCHAR(255),
               points INTEGER,
               attempts INTEGER
               );
               """)

connect.commit()


class User:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = 0
        self.email = None
        self.password = None
        self.points = 0
        self.attempts = 0

    def main(self):
        self.name = input("Введите ваше имя: ")
        self.surname = input("Введите вашу фамилию: ")
        self.age = int(input("Введите ваш возраст: "))
        self.email = input("Введите вашу почту: ")
        self.password = input("Введите пароль: ")
        password_rest = input("Подтвердите пароль: ")
        self.points = 0
        self.attempts = 0

        if self.age < 18:
            print("Регистрация не прошла, вам нет 18 лет!!!")
            self.main()
        else:
            if self.password == password_rest:
                cursor.execute(f""" INSERT INTO clients (name, surname, age, email, password,  points, attempts)
                       VALUES(  '{self.name}', '{self.surname}',' {self.age}', '{self.email}', '{self.password}', '{self.points}', '{self.attempts}');""")
                connect.commit()

                print(f"Уважаемый {self.name} {self.surname}, вы успешно прошли регистрацию")
                print("Игра начинается!!!")
                print()
                self.game()

    def game(self):
        ball = 0
        limit = 5
        while True:
            randon = random.randint(1,5)
            user = int(input("Введите число: "))
            if limit == 0:
                print(f"Вы проиграли, у вас закончились попытки. Баллы за  победу: {ball}, Количество попыток: {limit}")
                break
            else:
                if ball == 5:
                    print(f"Вы выиграли, у вас 5 баллов!!. Баллы за  победу: {ball}, Количество попыток: {limit}")
                    break
                else:
                    if user == randon:
                        ball+=1
                        print(f"Вы угадали, Бот выбрал: {randon}. Выигрыш: {ball}. Количество попыток: {limit}")
                    else:
                        limit -=1
                        print(f"Вы не угадали, Бот выбрал: {randon}. Выигрыш: {ball}. Количество попыток: {limit}")
            cursor.execute(f'''UPDATE clients SET points = {ball}, attempts = {5 - limit} WHERE name = "{self.name}"''')
            connect.commit()
            


user = User()
user.main()

