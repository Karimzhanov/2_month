import sqlite3

connect = sqlite3.connect('book.db')
cursor = connect.cursor()

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")


    cursor.execute("""CREATE TABLE IF NOT EXISTS Book(
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                year INTEGER
    );""")
    connect.commit()
    
    def display_books(self):
        cursor.execute('''SELECT * FROM Book''')
        books = cursor.fetchall()
        for book in books:
            print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год выпуска: {book[3]}")
        connect.commit()


    def update_book(self, old_title, new_title, new_author, new_year):
     cursor.execute(f"""UPDATE Book SET title = ?, author = ?, year = ? WHERE title = ?""",
                   ('{self.new_title}', '{self.new_author}', '{self.new_year}', '{self.old_title}'))
    connect.commit()

    def add_book(self):
        cursor.execute(f'''INSERT INTO Book(title, author, year)
                       VALUES("{self.title}", '{self.author}', '{self.year}');''')
        connect.commit()

    def delete_book(self, title):
        cursor.execute('''DELETE FROM Book WHERE title = ?''', (title,))
        connect.commit()




book1 = Book('13','13',13) 
book = Book('12','12',12)
book.display_info()
book.display_books()
book.add_book() 
book.update_book('старое_название', 'новое_название', 'новый_автор', 'новый_год')
book.delete_book('')


book1.display_info()
book1.display_books()
book1.add_book()
book1.update_book('старое_название', 'новое_название', 'новый_автор', 'новый_год')
book1.delete_book('13')

