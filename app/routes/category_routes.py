from flask import Blueprint, request, jsonify
from app.db.session import SessionLocal
from app.models.category import Category

router = Blueprint("category", __name__, url_prefix="/categories")

@router.route("/", methods=["GET"])
def get_categories():
    db = SessionLocal()
    categories = db.query(Category).all()
    result = [{"id": c.id, "name": c.name} for c in categories]
    db.close()
    return jsonify(result)

@router.route("/", methods=["POST"])
def create_category():
    data = request.get_json()
    db = SessionLocal()
    new_category = Category(name=data.get("name"))
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    db.close()
    return jsonify({"id": new_category.id, "message": "Category created"}), 201
