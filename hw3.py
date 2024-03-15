class User:
    def __init__(self, name, email,  password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        pass


class Student(User):
    def __init__(self, name, email,  password, student_id):
        self.name = name
        self.email = email
        self.password = password
        self.student_id = student_id
        self.courses_enrolled = []

    def enroll_in_course(self, course):
        self.courses_enrolled.append(course)

    def info(self):
        print(f'{self.courses_enrolled}, Muhammadumar')
    

class Teacher(User):
    def __init__(self, name, email, password, teacher_id):
        self.name = name
        self.email = email
        self.password = password
        self.teacher_id = teacher_id
        self.courses_teaching = []

    def info(self):
        print(f'{self.courses_teaching}, Nurbolot')

    def assign_grade(self, student, course, grade):
        pass


class Admin(User):
    def __init__(self, name, email, password, admin_id):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin_id
        

    def create_course(self, curse_name):
        self.curse_name = curse_name 

    def info(self):
        print(f'{self.curse_name}, admin')

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, email, password, teacher_id,student_id):
        Student.__init__(self, name, email,  password, student_id)
        Teacher.__init__(self, name, email, password, teacher_id)
        self.teacher_id = teacher_id
        self.student_id = student_id

    def info(self):
        print(f'{self.teachingAssistant}, Nurai')


student = Student("Мухаммадумар", "karimzhanov@gmail.com", "password", "S13d45")
teacher = Teacher("Нурболот", "Hurbolot@gmail.com", "password456", "T9a8765")
admin = Admin("Администратор", "admin@gmail.com", "adminpassword", "A54c321")
teachingassistant = TeachingAssistant("Нурай", "Nurai@gmail.com", "password", "S6e3890", "T9a8765")

student.enroll_in_course("Backend, 'front")
teacher.assign_grade(student, "Backend", 10)
admin.create_course("java")     

student.info()
teacher.info()
admin.info()
