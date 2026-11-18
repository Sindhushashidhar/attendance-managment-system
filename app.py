from flask_login import current_user
from flask import Flask, redirect, url_for
from flask_login import LoginManager
from models.models import db, User
from routes.auth_routes import auth
from routes.teacher_routes import teacher
from routes.student_routes import student

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
app.register_blueprint(teacher)
app.register_blueprint(student)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    if current_user.is_authenticated:
        if current_user.role == 'teacher':
            return redirect(url_for('teacher.dashboard'))
        return redirect(url_for('student.my_attendance'))
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)