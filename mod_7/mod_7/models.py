from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship("Student", back_populates="group")


class Lecturer(Base):
    __tablename__ = "lecturers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    lecturer_id = Column(Integer, ForeignKey("lecturers.id"))
    lecturer = relationship("Lecturer", back_populates="subjects")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    grade = Column(Float, nullable=False)
    date_received = Column(Date, nullable=False)
    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")


Student.group = relationship("Group", back_populates="students")
Student.grades = relationship("Grade", back_populates="student")
Lecturer.subjects = relationship("Subject", back_populates="lecturer")
Subject.grades = relationship("Grade", back_populates="subject")
