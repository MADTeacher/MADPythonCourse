import os

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session as SQLSession

from models.database import DATABASE_NAME, Session
import create_database as db_creator
from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group


class MyException(Exception):
    ...


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session: SQLSession = Session()
    try:
        student = session.query(Student).get(20)
        print(student)
        # student.age = 16
        session.query(Student).update({Student.age: Student.age + 1})
        print(student)
        session.query(Student).filter(Student.age <= 18).update({Student.age: Student.age + 1})
        print(student)
        # session.delete(student)
        print(f'Кол-во студентов: {session.query(Student).count()}')
        session.query(Student).filter(Student.surname.like('Р%')).delete(synchronize_session='fetch')
        print(f'Кол-во студентов: {session.query(Student).count()}')
        raise MyException("Boom!!!")
        session.commit()
    except MyException:
        session.rollback()
        print(f'Кол-во студентов: {session.query(Student).count()}')
    finally:
        session.close()





