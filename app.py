from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key'  # Change this to a secure secret key in production

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def home():
    if 'username' in session:
        #return f'Hello, {session["username"]}! <a href="/logout">Logout</a>'
        return render_template('welcome.html')
    else:
        #return 'Welcome to the login page. <a href="/login">Login</a>'
        return render_template('welcome.html')
        
    
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your username and password.', 'error')

    return render_template('login.html')

""" @app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home')) """

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
