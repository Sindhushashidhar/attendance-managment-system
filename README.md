# Attendance Management System

A web application that lets teachers create classes, add students and mark daily attendance, and lets students log in to view their own attendance. Built with Flask and SQLite.

## Features

**Teacher**
- Register and log in securely (passwords are hashed)
- Create and manage classes
- Add students to a class (creates a login for each student)
- Mark daily attendance by date, with live Present/Absent counters
- Re-open any date to edit attendance without creating duplicates
- Attendance report with a bar chart, class average and date-range filter
- Automatic red warning for students below 75% attendance

**Student**
- Log in to a personal dashboard
- See overall attendance percentage, days present and days absent
- View full attendance history
- Warning message when attendance is below 75%

**Security**
- Role-based access: students cannot open teacher pages
- A teacher can only access their own classes

## Tech Stack

| Part | Technology |
|------|------------|
| Backend | Python, Flask |
| Database | SQLite with Flask-SQLAlchemy |
| Authentication | Flask-Login, Werkzeug password hashing |
| Frontend | HTML, Jinja2 templates, Bootstrap 5, Bootstrap Icons |
| Charts | Chart.js |

## Screenshots

### Login and Home

| Login Page | Home Page |
|---|---|
| ![Login Page](screenshots/login%20page.png) | ![Home Page](screenshots/home%20page.png) |

### Teacher

| Adding a Student | Marking Attendance |
|---|---|
| ![Adding Student](screenshots/adding%20student.png) | ![Marking Attendance](screenshots/marking%20attendance.png) |

| Attendance Report | Students Attendance List |
|---|---|
| ![Attendance Report](screenshots/attendance%20report.png) | ![Students Attendance List](screenshots/students%20attendance%20list.png) |

### Student

![Student Attendance](screenshots/student%20attendance.png)

## Database Design

- **User**: id, name, email, password_hash, role (teacher or student)
- **StudentClass**: id, class_name, teacher_id
- **Student**: id, user_id, roll_number, class_id
- **Attendance**: id, student_id, class_id, date, status (present or absent)

## Project Structure

```
attendance-managment-system/
├── app.py
├── requirements.txt
├── models/
│   └── models.py
├── routes/
│   ├── auth_routes.py
│   ├── teacher_routes.py
│   └── student_routes.py
└── templates/
    ├── base.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── create_class.html
    ├── view_class.html
    ├── add_student.html
    ├── mark_attendance.html
    ├── report.html
    └── student_dashboard.html
```

## How to Run Locally

1. Clone the repository
```
git clone https://github.com/Sindhushashidhar/attendance-managment-system.git
cd attendance-managment-system
```

2. Create and activate a virtual environment (Windows)
```
python -m venv venv
venv\Scripts\activate
```

3. Install the requirements
```
pip install -r requirements.txt
```

4. Start the app
```
python app.py
```

5. Open http://127.0.0.1:5000 in your browser.

## How to Use

1. Register a **Teacher** account and log in.
2. Create a class, then add students with a roll number and a temporary password.
3. Open the class and click **Mark Attendance** to record a day.
4. Click **Report** to see percentages and the chart.
5. Log out and log in with a student's email and password to see the student view.

## Future Improvements

- Export reports to CSV or PDF
- Email alerts to students with low attendance
- Let students change their temporary password
- Admin role to manage teachers
- Deploy online with PostgreSQL

## Author

**Sindhu Shashidhar**
Lecturer | Aspiring Software Developer

GitHub: [Sindhushashidhar](https://github.com/Sindhushashidhar)