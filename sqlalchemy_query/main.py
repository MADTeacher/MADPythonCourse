import os

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session as SQLSession

from models.database import DATABASE_NAME, Session
import create_database as db_creator
from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session: SQLSession = Session()
    print(f'Кол-во студентов: {session.query(Student).count()}')
    student = session.query(Student).filter(and_(Student.surname.like('Д%'), Student.age > 18)).one()
    print(student)
    print('*'*30)
    students = session.query(Student).filter(and_(Student.surname.like('А%'), Student.age > 16))
    for it in students:
        print(it)
    print('*' * 30)
    students_list: list[Student] = [it for it in students]
    print(students_list)
    print('*'*30)
    for it in session.query(Student).filter(or_(Student.surname.like('Д%'), Student.surname.like('В%'))):
        print(it)
    print('*' * 30)
    student_query = session.query(Student).join(Group).filter(Group.group_name == '1-МДА-9')
    for it in student_query:
        print(it)
    print(f'Кол-во студентов: {student_query.count()}')
    print('*' * 30)
    for it in session.query(Lesson):
        print(it)
    print('*' * 30)
    for it in session.query(Lesson).filter(Lesson.id > 3):
        print(it)
    print('*' * 30)
    for it in session.query(Lesson).filter(and_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
        print(it)
    print('*' * 30)
    for it, _ in session.query(Lesson.lesson_title, Group.group_name).filter(and_(
        association_table.c.lesson_id == Lesson.id,
        association_table.c.group_id == Group.id,
        Group.group_name == '1-МДА-7'
    )):
        print(it)
    print('*' * 30)
    print(session.query(Student).get(40))
    print(session.query(Student).get(60))

    session.close()








