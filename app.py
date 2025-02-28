from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
from email_service import email_blueprint, init_mail
import os

# Initialize the app
app = Flask(__name__)

# Инициализация почтового сервера
init_mail(app)

# Загрузка конфигурации из файла
try:
    app.config.from_pyfile("config.py")
except FileNotFoundError:
    print("Ошибка: файл конфигурации config.py не найден.")
    exit(1)

# Инициализация почтового сервера
mail = Mail(app)

# Инициализация CORS
CORS(app)

# Подключение к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/buibui'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Регистрация Blueprint для email
app.register_blueprint(email_blueprint, url_prefix="/email")

# Инициализация базы данных
db = SQLAlchemy(app)

# Импорт маршрутов
from routes import *

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()  # Создание таблиц, если они еще не существуют
        except Exception as e:
            print(f"Ошибка при создании таблиц: {e}")
            exit(1)

    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
        exit(1)
