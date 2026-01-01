import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sumit123",
        database="hostelsphere"
    )

from flask import session, flash

# "pip install mysql-connector-python" in powershell
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sumit123",
    database="hostelsphere"
)

cursor = db.cursor()

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "hostelsphere_secret_key"
resident_counter = 1


@app.route("/")
def home():
    return render_template("index.html")   # front page 
    


@app.route("/login")
def login():
    return render_template("login.html") #login page


@app.route("/register-hostel", methods=["GET", "POST"])
def register_hostel():
    if request.method == "POST":
        incharge_name = request.form["incharge_name"]
        hostel_name = request.form["hostel_name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        # generate hostel_id safely
        cursor.execute("SELECT COUNT(*) FROM hostels")
        count = cursor.fetchone()[0] + 1
        hostel_id = f"SPHERE{count:04d}"
        username = hostel_id

        cursor.execute("""
            INSERT INTO hostels
            (hostel_id, username, incharge_name, hostel_name, email, password)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (hostel_id, username, incharge_name, hostel_name, email, password))

        conn.commit()
        cursor.close()
        conn.close()

        return render_template("dashboard.html", hostel_id=hostel_id)

    return render_template("register_hostel.html")





@app.route("/register-resident", methods=["GET", "POST"])
def register_resident():
    if request.method == "POST":
        cursor.execute("SELECT COUNT(*) FROM residents")
        count = cursor.fetchone()[0] + 1
        resident_id = f"RES{count:04d}"

        cursor.execute("""
            INSERT INTO residents
            (resident_id, name, age, gender, phone, father_name, address, nationality)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            resident_id,
            request.form["name"],
            request.form["age"],
            request.form["gender"],
            request.form["phone"],
            request.form["father"],
            request.form["address"],
            request.form["nationality"]
        ))

        db.commit()
        return f"Registration successful! Your Resident ID is {resident_id}"

    return render_template("register_resident.html")





@app.route("/login-hostel", methods=["GET", "POST"])
def login_hostel():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM hostels WHERE username = %s",
            (username,)
        )
        hostel = cursor.fetchone()
        cursor.close()

        # Invalid username
        if hostel is None:
            return "Invalid username or password"

        # Invalid password
        if hostel["password"] != password:
            return "Invalid username or password"

        # Successful login → save session
        session["hostel_id"] = hostel["hostel_id"]
        session["hostel_name"] = hostel["hostel_name"]

        return redirect(url_for("dashboard"))

    return render_template("login_hostel.html")





@app.route("/dashboard")
def dashboard():
    # 🔒 Protect route
    if "hostel_id" not in session:
        return redirect(url_for("login_hostel"))

    hostel_id = session["hostel_id"]
    hostel_name = session["hostel_name"]

    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT resident_id, name, room_no, email
        FROM residents
        WHERE hostel_id = %s
    """, (hostel_id,))

    residents = cursor.fetchall()

    return render_template(
        "dashboard.html",
        hostel_name=hostel_name,
        residents=residents
    )






@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))





@app.route("/add-resident", methods=["POST"])
def add_resident():
    if "hostel_id" not in session:
        return redirect(url_for("login_hostel"))

    resident_id = request.form["resident_id"]
    hostel_id = session["hostel_id"]

    cursor = db.cursor()

    # Check if resident exists
    cursor.execute(
        "SELECT * FROM residents WHERE resident_id = %s",
        (resident_id,)
    )
    resident = cursor.fetchone()

    if resident is None:
        return "Resident not found"

    # LINK resident to hostel
    cursor.execute(
        "UPDATE residents SET hostel_id = %s WHERE resident_id = %s",
        (hostel_id, resident_id)
    )
    db.commit()

    return redirect(url_for("dashboard"))





if __name__ == "__main__":
    app.run(debug=True)
