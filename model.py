from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Result(db.Model):

	__tablename__ = "Results"

	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	url = db.Column(db.Text(), nullable=False)
	size = db.Column(db.Integer, nullable=False)
	datetime = db.Column(db.Integer, nullable=False)

# Helper functions
def connect_to_db(app):
	"""Connect the database to our Flask app."""

	# Configure to use our SQLite database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
	app.config['SQLALCHEMY_ECHO'] = True
	db.app = app
	db.init_app(app)


if __name__ == "__main__":
	# As a convenience, if we run this module interactively, it will leave
	# you in a state of being able to work with the database directly.

	# So that we can use Flask-SQLAlchemy, we'll make a Flask app
	from flask import Flask
	app = Flask(__name__)

	connect_to_db(app)
	print "Connected to DB."