from flask import Blueprint, request, jsonify
from app.db.session import SessionLocal
from app.models.lesson import Lesson

router = Blueprint("lesson", __name__, url_prefix="/lessons")

@router.route("/", methods=["GET"])
def get_lessons():
    db = SessionLocal()
    lessons = db.query(Lesson).all()
    result = []
    for l in lessons:
        result.append({
            "id": l.id,
            "title": l.title,
             "course_id": l.course_id,
            # İstersen category adı da çekilebilir
            # "category_name": l.category.name if l.category else None
        })
    db.close()
    return jsonify(result)

@router.route("/", methods=["POST"])
def create_lesson():
    data = request.get_json()
    db = SessionLocal()
    new_lesson = Lesson(
        title=data.get("title"),
        content=data.get("content"),
        course_id=data.get("course_id")
    )
    db.add(new_lesson)
    db.commit()
    db.refresh(new_lesson)
    db.close()
    return jsonify({"id": new_lesson.id, "message": "Lesson created"}), 201
