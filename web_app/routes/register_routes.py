from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Create a Flask web application
app = Flask(__name__)

# Configure the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Create a SQLAlchemy database instance
db = SQLAlchemy(app)

# Define a User class that represents a database table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # You can add more fields to this class as needed

# Define a route for the homepage
@app.route('/')
def home():
    return 'Welcome to the Book Exchange Platform!'

# Define a route for user registration with GET and POST methods
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        # Check if the user already exists in the database
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
        else:
            # Create a new User object and add it to the database
            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('home'))

    # Render an HTML template for user registration
    return render_template('register.html')

# Entry point for running the Flask app
if __name__ == '__main__':
    # Set the secret key for session management (change to a random secret key)
    app.secret_key = 'your_secret_key'

    # Create the database tables
    db.create_all()

    # Run the Flask app in debug mode
    app.run(debug=True)
