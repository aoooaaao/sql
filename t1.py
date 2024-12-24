import sqlite3
sqlite_connection = sqlite3.connect('sqlite_python.db')

students_tb = '''CREATE TABLE students (
    students_id INTEGER PRIMARY KEY AUTOINCREMENT,
    students_name TEXT NOT NULL,
    students_surname TEXT NOT NULL,
    students_age INTEGER NOT NULL,
    students_city TEXT NOT NULL);'''

courses_tb = '''CREATE TABLE courses (
    courses_id INTEGER PRIMARY KEY AUTOINCREMENT,
    courses_name TEXT NOT NULL,
    courses_time_start TEXT NOT NULL,
    courses_time_end TEXT NOT NULL);'''

Student_courses_tb = '''CREATE TABLE Student_courses (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(students_id), 
    FOREIGN KEY (course_id) REFERENCES courses(courses_id),
    PRIMARY KEY (student_id, course_id));'''

cursor = sqlite_connection.cursor()

print("База данных подключена к SQLite")
cursor.execute(students_tb)
cursor.execute(courses_tb)
cursor.execute(Student_courses_tb)
sqlite_connection.commit()
sqlite_connection.close()