from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from models import Student, Grade, Subject, Group, Lecturer

engine = create_engine("postgresql://postgres:mypassword@localhost:5432/mydatabase")
Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    return (
        session.query(Student.name, func.avg(Grade.grade).label("average_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
    )


def select_2(subject_id):
    return (
        session.query(Student.name, func.avg(Grade.grade).label("average_grade"))
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(1)
        .one()
    )


def select_3(subject_id):
    return (
        session.query(Group.name, func.avg(Grade.grade).label("average_grade"))
        .join(Student, Group.students)
        .join(Grade, Student.grades)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )


def select_4():
    return (
        session.query(Group.name, func.avg(Grade.grade).label("average_grade"))
        .join(Student, Group.students)
        .join(Grade, Student.grades)
        .group_by(Group.id)
        .all()
    )


def select_5(lecturer_id):
    return session.query(Subject.name).filter(Subject.lecturer_id == lecturer_id).all()


def select_6(group_id):
    return session.query(Student.name).filter(Student.group_id == group_id).all()


def select_7(group_id, subject_id):
    return (
        session.query(Student.name, Grade.grade)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )


def select_8(lecturer_id):
    return (
        session.query(func.avg(Grade.grade).label("average_grade"))
        .join(Subject)
        .filter(Subject.lecturer_id == lecturer_id)
        .all()
    )


def select_9(student_id):
    return (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .group_by(Subject.id)
        .all()
    )


def select_10(lecturer_id, student_id):
    return (
        session.query(Subject.name)
        .join(Grade)
        .filter(Subject.lecturer_id == lecturer_id, Grade.student_id == student_id)
        .group_by(Subject.id)
        .all()
    )


session.close()
