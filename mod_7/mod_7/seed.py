import random
from datetime import datetime
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Lecturer, Subject, Grade

fake = Faker()

engine = create_engine("postgresql://postgres:mypassword@localhost:5432/mydatabase")
Session = sessionmaker(bind=engine)
session = Session()


def create_groups():
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)
    session.commit()
    return groups


def create_students(groups):
    students = []
    for _ in range(50):
        group = random.choice(groups)
        students.append(Student(name=fake.name(), group=group))
    session.add_all(students)
    session.commit()
    return students


def create_lecturers():
    lecturers = [Lecturer(name=fake.name()) for _ in range(5)]
    session.add_all(lecturers)
    session.commit()
    return lecturers


def create_subjects(lecturers):
    subjects = [
        Subject(name=f"Subject {i}", lecturer=random.choice(lecturers))
        for i in range(1, 9)
    ]
    session.add_all(subjects)
    session.commit()
    return subjects


def create_grades(students, subjects):
    for student in students:
        for _ in range(20):
            subject = random.choice(subjects)
            grade = Grade(
                student=student,
                subject=subject,
                grade=random.uniform(2, 5),
                date_received=fake.date_this_year(),
            )
            session.add(grade)
    session.commit()


groups = create_groups()
students = create_students(groups)
lecturers = create_lecturers()
subjects = create_subjects(lecturers)
create_grades(students, subjects)

session.close()
