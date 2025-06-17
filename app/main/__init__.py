# app/__init__.py
from flask import Flask
from app.db.session import SessionLocal
from app.models import user  # Modelleri import et (migrations için önemli)

#python app/main.py
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Online Eğitim Platformu API Aktif ✅"

    return app
