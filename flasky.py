from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

recipes = []

@app.route("/")
def index():
	return "Hello world!"
	
if __name__ == "__main__":
	app.run()