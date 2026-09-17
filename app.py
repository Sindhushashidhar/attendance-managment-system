from flask import Flask
from flask_login import LoginManager
from models.models import db, User
from routes.auth_routes import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SECRET_KEY'] = 'change-this-later-to-something-random'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'Hello, Attendance System! You are logged in.'

if __name__ == '__main__':
    app.run(debug=True)