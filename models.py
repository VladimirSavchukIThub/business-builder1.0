from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Plot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)  # Ссылка на изображение
    price = db.Column(db.Float, nullable=False)  # Поле для цены участка

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "size": self.size,
            "image_url": self.image_url,  # Возвращаем ссылку на изображение
            "price": self.price  # Возвращаем цену участка
        }

class BusinessType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)  # Поле для ссылки на изображение
    description = db.Column(db.String(200), nullable=True)  # Поле для описания

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url,  # Возвращаем ссылку на изображение
            "description": self.description  # Возвращаем описание
        }
class BusinessConfiguration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_type_id = db.Column(db.Integer, db.ForeignKey('business_type.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)

    business_type = db.relationship('BusinessType', backref='configurations')

    def to_dict(self):
        return {
            "id": self.id,
            "business_type_id": self.business_type_id,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "is_admin": self.is_admin
        }