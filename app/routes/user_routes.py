from flask import Blueprint, jsonify, request
from app.db.session import SessionLocal
from app.models.user import User
from app.models.course import Course
from werkzeug.security import generate_password_hash

router = Blueprint("user", __name__)

@router.route("/users", methods=["GET"])
def list_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@router.route("/users/<int:user_id>/enroll", methods=["POST"])
def enroll_user_in_course(user_id):
    db = SessionLocal()

    data = request.get_json()
    course_id = data.get("course_id")

    user = db.query(User).get(user_id)
    course = db.query(Course).get(course_id)

    if not user or not course:
        db.close()
        return jsonify({"error": "Kullanıcı veya kurs bulunamadı"}), 404

    if course in user.enrolled_courses:
        db.close()
        return jsonify({"message": "Zaten bu kursa kayıtlı"}), 400

    user.enrolled_courses.append(course)
    db.commit()

    user_name = user.name
    course_title = course.title

    db.close()

    return jsonify({"message": f"{user_name} kullanıcısı '{course_title}' kursuna başarıyla kayıt oldu"})


@router.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data.get("name") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "name, email ve password zorunlu"}), 400

    db = SessionLocal()
    # Aynı email var mı kontrolü (opsiyonel ama önerilir)
    if db.query(User).filter(User.email == data["email"]).first():
        db.close()
        return jsonify({"error": "Bu email zaten kayıtlı"}), 400

    hashed_password = generate_password_hash(data["password"])
    new_user = User(
        name=data["name"],
        email=data["email"],
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return jsonify({
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }), 201