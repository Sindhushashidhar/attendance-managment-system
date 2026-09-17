from werkzeug.security import generate_password_hash
from models.models import User, Student
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models.models import db, StudentClass

teacher = Blueprint('teacher', __name__)

@teacher.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'teacher':
        return "Access denied. Teachers only.", 403

    classes = StudentClass.query.filter_by(teacher_id=current_user.id).all()
    return render_template('dashboard.html', classes=classes)

@teacher.route('/create-class', methods=['GET', 'POST'])
@login_required
def create_class():
    if current_user.role != 'teacher':
        return "Access denied. Teachers only.", 403

    if request.method == 'POST':
        class_name = request.form['class_name']
        new_class = StudentClass(class_name=class_name, teacher_id=current_user.id)
        db.session.add(new_class)
        db.session.commit()
        flash('Class created successfully!')
        return redirect(url_for('teacher.dashboard'))

    return render_template('create_class.html')
@teacher.route('/class/<int:class_id>/add-student', methods=['GET', 'POST'])
@login_required
def add_student(class_id):
    if current_user.role != 'teacher':
        return "Access denied. Teachers only.", 403

    class_obj = StudentClass.query.get_or_404(class_id)
    if class_obj.teacher_id != current_user.id:
        return "Access denied. Not your class.", 403

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        roll_number = request.form['roll_number']
        password = request.form['password']

        existing = User.query.filter_by(email=email).first()
        if existing:
            flash('A user with this email already exists.')
            return redirect(url_for('teacher.add_student', class_id=class_id))

        new_user = User(
            name=name,
            email=email,
            password_hash=generate_password_hash(password),
            role='student'
        )
        db.session.add(new_user)
        db.session.commit()

        new_student = Student(
            user_id=new_user.id,
            roll_number=roll_number,
            class_id=class_id
        )
        db.session.add(new_student)
        db.session.commit()

        flash(f'Student {name} added to {class_obj.class_name}!')
        return redirect(url_for('teacher.view_class', class_id=class_id))

    return render_template('add_student.html', class_obj=class_obj)

@teacher.route('/class/<int:class_id>')
@login_required
def view_class(class_id):
    if current_user.role != 'teacher':
        return "Access denied. Teachers only.", 403

    class_obj = StudentClass.query.get_or_404(class_id)
    if class_obj.teacher_id != current_user.id:
        return "Access denied. Not your class.", 403

    students = Student.query.filter_by(class_id=class_id).all()
    return render_template('view_class.html', class_obj=class_obj, students=students)