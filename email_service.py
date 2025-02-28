from flask import Blueprint, request, jsonify
from flask_mail import Mail, Message
import traceback  # Для более детального логирования ошибок

# Создаем Blueprint для обработки email
email_blueprint = Blueprint("email_service", __name__)

# Инициализация почтового сервера
mail = Mail()

# Настройки почтового сервера
def init_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.mail.ru'  # Используйте ваш почтовый сервер
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'biznes.prilozheniye@mail.ru'  # Замените на ваш логин
    app.config['MAIL_PASSWORD'] = 'mzV9zVHhQCsgd9g4CL4E'  # Замените на ваш пароль
    app.config['MAIL_DEFAULT_SENDER'] = 'biznes.prilozheniye@mail.ru'  # Укажите свой отправитель

    mail.init_app(app)

# Маршрут для отправки email
@email_blueprint.route("/send-email", methods=["POST"])
def send_email():
    data = request.json

    # Проверяем наличие всех необходимых данных
    email = data.get("email")
    business_type = data.get("business_type")  # Если не передано, по умолчанию "Не указано"
    customer_name = data.get("name")
    customer_surname = data.get("surname")
    total_price = data.get("totalPrice")

    # Проверка обязательных данных
    if not email or not customer_name or not customer_surname or not total_price:
        return jsonify({"error": "Все поля (email, имя, фамилия, цена) обязательны"}), 400

    # Создание сообщения
    msg = Message("Подтверждение выбора конфигурации", recipients=[email])
    msg.body = f"""
    Здравствуйте, {customer_name} {customer_surname}!

    Вы выбрали конфигурацию: {business_type}
    Итоговая цена(конфигурации без стоимости участка): {total_price} руб.

    В ближайшее время менеджер свяжется с Вами.
    
    Спасибо за использование нашего сервиса!
    """

    try:
        # Отправка письма
        mail.send(msg)
        return jsonify({"message": "Письмо отправлено!"})
    except Exception as e:
        # Логирование ошибки с полным стектрейсом
        error_message = str(e)
        error_traceback = traceback.format_exc()
        print(f"Ошибка при отправке письма: {error_message}")
        print(f"Полный traceback: {error_traceback}")
        return jsonify({"error": f"Ошибка при отправке письма: {error_message}", "traceback": error_traceback}), 500
