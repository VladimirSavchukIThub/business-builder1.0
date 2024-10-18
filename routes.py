from flask import request, jsonify
from app import app, db
from models import Plot, BusinessType, BusinessConfiguration, User

# Добавление участка
@app.route('/add_data_plot', methods=['POST'])
def add_data_plot():
    data = request.get_json()
    required_fields = ('name', 'location', 'size', 'image_url', 'price')
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    plot = Plot(
        name=data['name'],
        location=data['location'],
        size=data['size'],
        image_url=data['image_url'],
        price=data['price']
    )
    db.session.add(plot)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Участок успешно добавлен", "plot": plot.to_dict()}), 201

# Добавление типа бизнеса
@app.route('/add_data_business_type', methods=['POST'])
def add_data_business_type():
    data = request.get_json()
    required_fields = ('name', 'image_url', 'description')
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    business_type = BusinessType(
        name=data['name'],
        image_url=data['image_url'],
        description=data['description']
    )

    db.session.add(business_type)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Тип бизнеса успешно добавлен", "business_type": business_type.to_dict()}), 201

# Добавление конфига(пока не работает)
@app.route('/add_business_configuration', methods=['POST'])
def add_business_configuration():
    data = request.get_json()
    if not all(key in data for key in ('business_type_id', 'name', 'price')):
        return jsonify({"error": "Missing fields"}), 400

    business_configuration = BusinessConfiguration(
        business_type_id=data['business_type_id'],
        name=data['name'],
        description=data.get('description', ''),
        price=data['price']
    )
    db.session.add(business_configuration)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    return jsonify({'message': 'Configuration added successfully.'}), 201

# Получение участков
@app.route('/plots', methods=['GET'])
def get_plots():
    plots = Plot.query.all()
    return jsonify([plot.to_dict() for plot in plots]), 200

# Получение типов бизнеса
@app.route('/business_types', methods=['GET'])
def get_business_types():
    business_types = BusinessType.query.all()
    return jsonify([business_type.to_dict() for business_type in business_types]), 200

# Создание админа
@app.route('/api/add_admin', methods=['POST'])
def add_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Проверка на существование пользователя
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    # Создание нового администратора
    new_admin = User(username=username, is_admin=True)
    new_admin.set_password(password)  # Задаем зашифрованный пароль

    db.session.add(new_admin)
    db.session.commit()

    return jsonify({"message": "Admin added successfully"}), 201

# Вход под админом
@app.route('/api/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    print(f"Attempting to authenticate user: {username}")  # Логирование

    # Проверяем, существует ли пользователь
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"success": False, "message": "User does not exist"}), 401

    # Проверяем, является ли пользователь администратором
    if not user.is_admin:
        return jsonify({"success": False, "message": "User is not an admin"}), 401

    # Проверяем пароль
    if user.check_password(password):
        return jsonify({"success": True, "message": "Authenticated", "user": user.to_dict()})

    return jsonify({"success": False, "message": "Invalid credentials"}), 401


# Добавление участка админом
@app.route('/api/plots', methods=['POST'])
def add_plot():
    data = request.get_json()
    if not all(key in data for key in ('name', 'location', 'size', 'price', 'image_url')):
        return jsonify({"error": "Missing fields"}), 400

    new_plot = Plot(
        name=data['name'],
        location=data['location'],
        size=data['size'],
        price=data['price'],
        image_url=data['image_url']
    )
    db.session.add(new_plot)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)
