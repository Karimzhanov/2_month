# Задача 1
# class Student:
#     def __init__(self, name, lastname, student_id):
#         self.name = name
#         self.lastname = lastname
#         self.student_id = student_id
#         self.courses = []

#     def add_course(self, course):
#         if course not in self.courses:
#             self.courses.append(course)
#             print(f"Курс {course} добавлен для студента {self.lastname}")
#         else:
#             print(f"Студент {self.lastname}уже посещает курс {course}.")

#     def remove_course(self, course):
#         if course in self.courses:
#             self.courses.remove(course)
#             print(f"Курс {course} удален для студента {self.lastname}")
#         else:
#             print(f"Студент {self.lastname} не посещает курс {course}.")

#     def info(self):
#         print (f"Student: {self.name} {self.lastname}, ID: {self.student_id}, Courses: {self.courses}")

# student = Student('Каримжанов',' Мухаммадумар', 33142233)
# student1 = Student('Нурай ','Темирбаева', 33142244, )

# student.add_course("java")
# student.add_course("python")
# student.remove_course('java')

# student1.add_course("java")
# student1.add_course("python")
# student1.remove_course('java')


# student.info()
# student1.info()





#  Задача2
# class Library:
#     def __init__(self, name, author, status ):
#         self.name = name
#         self.author = author
#         self.status = status
#         self.books = []

#     def add_books(self, books):
#         if books not in self.books:
#             self.books.append(books)
#             print(f"{books} добавлен ")
#         else:
#             print(f"уже {books} существует")
       

#     def remove_books(self, books):
#         if books in self.books:
#             self.books.remove(books)
#             print(f" книга '{books}' удалена ")
#         else:
#             print(f"Такой книги нет")


#     def info(self):
#         print (f"Имя книги:, '{self.name}', Автор:, '{self.author}', Статус:, '{self.status}', добавленная книга {self.books} ")

# book = Library('Гарри Поттер и узник Азкабан', 'Евгений Замятин', 'доступна')
# book.add_books(['В конце они оба умрут', 'Под полящим солнцем'])

# book.remove_books('Под полящим солнцем')
# book.info()


# Задача 3
# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print (3.14 * self.radius ** 2)

# class Square(Shape):
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def area(self):
#         print (self.side_length ** 2)

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         print( self.base * self.height / 2)




# chape = Circle(2)
# chape.area()
        
# chape = Square(2)
# chape.area()

        
# chape = Triangle(2,3)
# chape.area()