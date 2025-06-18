from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.user_course import user_course  # önceki many-to-many için
# Aşağıyı da eklersen hazır olur:
from app.models.category import Category  # kategori ilişkilendirme için

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))  # dikkat! tablo adı categories
    user_id = Column(Integer, ForeignKey("users.id"))

    # Eğitmen (Many-to-One)
    instructor = relationship("User", back_populates="courses")

    # Öğrenciler (Many-to-Many)
    students = relationship("User", secondary=user_course, back_populates="enrolled_courses")

    # Kategori (Many-to-One)
    category = relationship("Category", back_populates="courses")
    
    lessons = relationship("Lesson", back_populates="course", cascade="all, delete-orphan")

