# app/models/course.py

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    ##category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey("users.id"))  # Eğitmen

    # Opsiyonel: İlişkiler (relationship) - eğitim veren kullanıcı ve kategori ile bağlantı
    instructor = relationship("User", back_populates="courses")

    #Kategory eklenince açılması lazım
    #category = relationship("Category", back_populates="courses")

    lessons = relationship("Lesson", back_populates="course", cascade="all, delete-orphan") #Course modelinin lesson ilişkisini tanıması için (one-to-many)

