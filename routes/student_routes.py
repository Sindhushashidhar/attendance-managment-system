from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.models import StudentClass, Student, Attendance

student = Blueprint('student', __name__)

@student.route('/my-attendance')
@login_required
def my_attendance():
    if current_user.role != 'student':
        return "Access denied. Students only.", 403

    record = Student.query.filter_by(user_id=current_user.id).first()
    if not record:
        return render_template('student_dashboard.html', record=None)

    class_obj = StudentClass.query.get(record.class_id)
    entries = Attendance.query.filter_by(student_id=record.id).order_by(Attendance.date.desc()).all()

    total = len(entries)
    present = sum(1 for e in entries if e.status == 'present')
    percent = round(present / total * 100) if total else 0

    return render_template(
        'student_dashboard.html',
        record=record,
        class_obj=class_obj,
        entries=entries,
        total=total,
        present=present,
        absent=total - present,
        percent=percent,
        low=total > 0 and percent < 75
    )