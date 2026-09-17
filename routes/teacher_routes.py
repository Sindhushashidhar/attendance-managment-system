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