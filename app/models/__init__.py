# app/models/__init__.py

from .user import User
from app.models import course

# Eğer daha sonra yeni modeller eklersen buraya da import etmen gerekir.
# Böylece Alembic `Base.metadata` içinden tüm tabloları görür.

from .category import Category
from .lesson import Lesson
