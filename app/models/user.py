from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.user_course import user_course  # burayı ekle

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    # Eğitmen olarak oluşturduğu kurslar
    courses = relationship("Course", back_populates="instructor")

    # Öğrenci olarak kayıtlı olduğu kurslar (many-to-many)
    enrolled_courses = relationship(
        "Course",
        secondary=user_course,
        back_populates="students"
    )
