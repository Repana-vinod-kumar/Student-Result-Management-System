# 🎓 Student Result Management System

A web-based Student Result Management System developed using Python, Flask, MySQL, HTML, CSS, and JavaScript. This application helps administrators manage student records, subjects, marks, and academic performance through an interactive dashboard.

## 📌 Project Overview

The Student Result Management System is designed to simplify student academic record management. It provides an organized platform for administrators to add student details, manage subjects, enter examination marks, and generate student performance reports.

The backend is developed using Python and Flask, while MySQL is used to store and manage student academic information.

## ✨ Key Features

- 🔐 Admin Login Authentication
- 👨‍🎓 Add and Manage Student Records
- 📚 Add and Manage Subjects
- 📝 Enter Student Examination Marks
- 📊 Calculate Student Results
- 📋 View Student Performance Reports
- 🔍 Search Students Using Hall Ticket Number
- 🗄️ MySQL Database Integration
- 📱 User-Friendly Admin Dashboard
- ⚡ Dynamic Web Application

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| Flask | Web Framework |
| MySQL | Database Management |
| HTML5 | Frontend Structure |
| CSS3 | UI Styling |
| JavaScript | Frontend Interactions |
| Bootstrap | Responsive UI (if used) |

## 📂 Project Structure

```text
Student-Result-Management-System/
│
├── app.py
├── database.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── admin_login.html
│   ├── dashboard.html
│   ├── add_student.html
│   ├── manage_student.html
│   ├── add_subject.html
│   ├── manage_subject.html
│   ├── enter_marks.html
│   └── report.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── database/
│   └── students_marks.sql
│
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Repana-vinod-kumar/Student-Result-Management-System.git
```

### Step 2: Navigate to Project Folder

```bash
cd Student-Result-Management-System
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure MySQL Database

1. Start MySQL using XAMPP or MySQL Server.
2. Create a database named `students_marks`.
3. Configure your database credentials in `database.py`.
4. Create the required database tables.

### Step 7: Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000/
```

## 🎯 Project Objectives

- Simplify student academic record management.
- Reduce manual examination result calculations.
- Maintain organized student information.
- Provide quick access to academic performance reports.
- Improve administrative efficiency.

## 🔮 Future Enhancements

- Student login portal.
- Downloadable PDF mark sheets.
- Automated grade calculation.
- Email notifications.
- Advanced student performance analytics.
- Cloud database integration.

## 👨‍💻 Developer

**Repana Vinod Kumar**

GitHub: https://github.com/Repana-vinod-kumar

## 📄 License

This project is developed for educational and learning purposes.
