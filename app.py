from flask import Flask, request, render_template
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vishnu@123",
    database="students_marks"
)
mycursor = mydb.cursor(dictionary=True)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def student_result():
    if request.method == "POST":

        hallticket = request.form["hallticket"]

        sql = "SELECT * FROM student WHERE hallticket = %s"
        mycursor.execute(sql, (hallticket,))

        student = mycursor.fetchone()
        if student:
            return render_template("result.html", student=student)
        else:
            return render_template("admin_login.html",
                                   message="Invalid Hall Ticket Number")

    return render_template("admin_login.html")

if __name__ == "__main__":
    app.run(debug=True)