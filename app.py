from flask import Flask, render_template, request
from models import db, DailyJobsModel, NormalJobsModel
import logging as logger
logger.basicConfig(level="DEBUG")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create tables before first request to the server (after deployment)
@app.before_first_request
def create_tables():
    db.create_all()

# Show the index page
@app.route('/')
def index():
    return render_template('index.html')

# Create Job (Retrieve Form & Hanlde the Post request from Form)
@app.route('/create', methods=['POST', 'GET'])
def create():
    pass

# Get all jobs for this comapny only
@app.route('/<string:company>/')
def readOne(company):
    pass

# Update Job (Retrieve Edit Form & Handle the Post request from Edit Form)
@app.route('/<int:id>/<string:type>/edit', methods=['POST', 'GET'])
def update(id, type):
    pass

# Delete a job from a table based on job id
@app.route('/<int:id>/<string:type>/delete')
def delete(id, type):
    pass

if __name__ == "__main__":
    logger.debug("Starting app service...")
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
