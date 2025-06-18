from flask import Blueprint, request, jsonify
from app.db.session import SessionLocal
from app.models.course import Course
from app.models.user import User
#from app.models.category import Category

router = Blueprint("course", __name__, url_prefix="/courses")

@router.route("/", methods=["GET"])
def get_courses():
    db = SessionLocal()
    courses = db.query(Course).all()
    result = []
    for c in courses:
        result.append({
            "id": c.id,
            "title": c.title,
            "description": c.description,
            "category": c.category.name if c.category else None,
            "instructor": c.instructor.name if c.instructor else None,
            "students": [student.name for student in c.students],  # öğrencilerin isimleri listesi
            "lessons": [{"id": lesson.id, "title": lesson.title} for lesson in c.lessons],  # derslerin kısa bilgisi
        })
    db.close()
    return jsonify(result)


@router.route("/", methods=["POST"])
def create_course():
    data = request.get_json()
    db = SessionLocal()
    new_course = Course(
        title=data.get("title"),
        description=data.get("description"),
        category_id=data.get("category_id"),
        user_id=data.get("user_id"),
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    db.close()
    return jsonify({"id": new_course.id, "message": "Course created"}), 201
