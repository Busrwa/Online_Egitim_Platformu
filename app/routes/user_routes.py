from flask import Blueprint, jsonify
from app.db.session import SessionLocal
from app.models.user import User

router = Blueprint("user", __name__)

@router.route("/users", methods=["GET"])
def list_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])
