from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Connect to SQLite Database
def connect_db():
    return sqlite3.connect('database.db')

# Route to display data
@app.route('/users')
def list_users():
    conn = connect_db()
    cur = conn.cursor()

    # Vulnerable SQL Query (SQL Injection risk)
    query = "SELECT * FROM users WHERE username = '" + request.args.get('username') + "'"
    cur.execute(query)
    users = cur.fetchall()

    conn.close()
    return render_template('users.html', users=users)

# Login Route (Insecure Authentication risk)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Vulnerable to simple password comparison (weak auth mechanism)
    if username == 'admin' and password == 'password123':
        return "Logged in as Admin!"
    else:
        return "Invalid credentials"

if __name__ == "__main__":
    app.run(debug=True)
