import sqlite3

sqlite_connection = sqlite3.connect('sqlite_python.db')
cursor = sqlite_connection.cursor()
print("База данных подключена к SQLite")

"""students_tb = '''INSERT INTO students
    (students_id, students_name, students_surname, students_age, students_city)
    VALUES (1, 'Max', 'Brooks', 24, 'Spb'),
    (2, 'John', 'Stones', 15, 'Spb'),
    (3, 'Andy', 'Wings', 45, 'Manhester'),
    (4, 'Kate', 'Brooks', 34, 'Spb')'''"""

"""courses_tb = '''INSERT INTO courses
    (courses_id, courses_name, courses_time_start, courses_time_end)
    VALUES (1, 'python', '2021-07-21', '2021-08-21'),
    (2, 'java', '2021-07-13', '2021-08-16')'''"""

"""Student_courses_tb = '''INSERT INTO Student_courses
    (student_id, course_id)
    VALUES (1, 1),
    (2, 1),
    (3, 1),
    (4, 2)'''"""

cursor.execute('SELECT students_name, students_age FROM Students WHERE students_age > 30;') # ищем старше 30
students_over_30 = cursor.fetchall() #что получили
print('Студенты старше 30 лет:', students_over_30)
cursor.execute("SELECT students_name FROM Students s JOIN Student_courses c ON s.students_id = c.student_id WHERE c.course_id = 1") # ищем тех, кто проходит курс
students_python = cursor.fetchall() # что получили
print('Студенты, которые проходят курс по питону:', students_python)
cursor.execute("SELECT students_name FROM Students s JOIN Student_courses c ON s.students_id = c.student_id WHERE c.course_id = 1 AND s.students_city = 'Spb'") # ищем тех, кто проходит курс и из спб
students_python_and_sbp = cursor.fetchall() # что получили
print('Студенты, которые проходят курс по питону и из Spb:', students_python_and_sbp)
sqlite_connection.commit()
sqlite_connection.close()