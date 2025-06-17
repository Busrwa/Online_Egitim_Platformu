from flask import Flask
from app.db.base import Base
from app.db.session import engine
from app.routes.user_routes import router as user_router  # aşağıda oluşturacaksın
from app.routes.course_routes import router as course_router
from app.routes.lesson_routes import router as lesson_router  # aşağıda oluşturacaksın
from app.routes.category_routes import router as category_routes

def create_app():
    app = Flask(__name__)

    # DB tablolarını oluştur
    Base.metadata.create_all(bind=engine)

    # Route’ları ekle
    app.register_blueprint(user_router)
    app.register_blueprint(course_router)
    app.register_blueprint(lesson_router)
    app.register_blueprint(category_routes)

    return app
