from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

# Initialize Flask app
app = Flask(__name__)
# Secret key for session management
app.secret_key = 'seccret_key'
# Database configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Initialize SQLAlchemy with Flask app
db = SQLAlchemy(app)
#database migrations
migrate = Migrate(app, db)

# User model definition for SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=True)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for login and signup page
@app.route('/loginsignup', methods=['GET', 'POST'])
def loginsignup():
    # Determine form type (login or signup) based on query parameter
    form_type = request.args.get('form_type', 'login')

    if request.method == 'POST':
        # Handle signup form submission
        if 'signup' in request.form:
            # Extract form data
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            phone = request.form['phone']
            gender = request.form['gender']
            #hash password
            hashed_password = generate_password_hash(password, method='sha256')

            #create new user instance and add to database
            new_user = User(name=name, email=email, password=hashed_password, phone=phone, gender=gender)
            db.session.add(new_user)
            db.session.commit()

            #success message
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('loginsignup', form_type='login'))

        # Handle login form submission
        elif 'login' in request.form:
            # Extract form data
            email = request.form['email']
            password = request.form['password']
            # Query database for user by email
            user = User.query.filter_by(email=email).first()
            # Check password and set session if valid
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['user_name'] = user.name
                flash('Login successful!', 'success')
                return render_template('index.html')
            else:
                flash('Login failed. Check your email and password.', 'danger')

    # Render login/signup template with form type 
    return render_template('loginsignup.html', form_type=form_type)

# amas vamatebdi da vegar movaswari
@app.route('/logout')
def logout():
    # washlis users
    session.pop('user_id', None)
    session.pop('user_name', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password='Lizuna777!',
    database="info"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT hotel_name, price FROM info")

myresult = mycursor.fetchall()

for x in myresult:
    hotel_name, price = x
    print(f"Hotel Name: {hotel_name}, Price: {price}")

#debug mode
if __name__ == '__main__':
    app.run(debug=True)

