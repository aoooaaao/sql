import sqlite3

class DatabaseManager:
    def __init__(self, db_name='sqlite_python.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        print("База данных подключена к SQLite")
        self.create_tables()
        self.insert_initial_data()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                surname TEXT NOT NULL,
                                age INTEGER NOT NULL,
                                city TEXT NOT NULL);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                time_start TEXT NOT NULL,
                                time_end TEXT NOT NULL);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Student_courses (
                                student_id INTEGER,
                                course_id INTEGER,
                                FOREIGN KEY (student_id) REFERENCES Students (id),
                                FOREIGN KEY (course_id) REFERENCES Courses (id),
                                PRIMARY KEY (student_id, course_id));''')
        self.connection.commit()
        print("Таблицы созданы")

    def insert_initial_data(self):
        courses_data = [
            (1, 'python', '21.07.21', '21.08.21'),
            (2, 'java', '13.07.21', '16.08.21')
        ]
        self.cursor.executemany('INSERT INTO Courses (id, name, time_start, time_end) VALUES (?, ?, ?, ?)', courses_data)

        students_data = [
            (1, 'Max', 'Brooks', 24, 'Spb'),
            (2, 'John', 'Stones', 15, 'Spb'),
            (3, 'Andy', 'Wings', 45, 'Manchester'),
            (4, 'Kate', 'Brooks', 34, 'Spb')
        ]
        self.cursor.executemany('INSERT INTO Students (id, name, surname, age, city) VALUES (?, ?, ?, ?, ?)', students_data)

        student_courses_data = [
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 2)
        ]
        self.cursor.executemany('INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)', student_courses_data)

        self.connection.commit()
        print("Данные успешно добавлены в таблицы.")

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def get_students_over_30(self):
        return self.execute_query('SELECT * FROM Students WHERE age > 30')

    def get_python_students(self):
        return self.execute_query('''SELECT s.*
                                      FROM Students s
                                      JOIN Student_courses sc ON s.id = sc.student_id
                                      JOIN Courses c ON sc.course_id = c.id
                                      WHERE c.name = ?''', ('python',))

    def get_python_students_from_spb(self):
        return self.execute_query('''SELECT s.*
                                      FROM Students s
                                      JOIN Student_courses sc ON s.id = sc.student_id
                                      JOIN Courses c ON sc.course_id = c.id
                                      WHERE c.name = ? AND s.city = ?''', ('python', 'Spb'))

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Соединение с SQLite закрыто")


def test_database_manager():
    db_manager = DatabaseManager()

    print("Студенты старше 30 лет:")
    students_over_30 = db_manager.get_students_over_30()
    print(students_over_30)

    print("Студенты, проходящие курс по Python:")
    python_students = db_manager.get_python_students()
    print(python_students)
    
    print("Студенты, проходящие курс по Python и из Spb:")
    python_students_spb = db_manager.get_python_students_from_spb()
    print(python_students_spb)

    db_manager.close_connection()