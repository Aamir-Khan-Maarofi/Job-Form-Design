import logging as logger
from models import db, JobsModel
from flask import Flask, current_app, render_template, request
logger.basicConfig(level="DEBUG")

app = Flask(__name__)
db.init_app(app)

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
    if request.method == "GET":
        return render_template('create.html')
    elif request.method == "POST":
        current_job = dict(request.form)
        job_type = "DAILY_JOBS" if form_data['type-of-trip'] == "daily-trips" else "NORMAL_JOB"
        print(current_job)
        if job_type == "DAILY_JOBS":
            print("[INFO: IT'S A DAILY TRIP]")
            # print("[INFO]: THERE ARE {} ENTRIES IN FORM DATA".format(len(current_job)))
            # Store to Database. 
            # this_job = DailyJobsModel(*current_job)
            # print(this_job)

            # job_type, meet_and_greet, flight_details, special_requiremetns as nulls
        
        if job_type == "NORMAL_JOB":
            print("[INFO]: IT'S A NORMAL TRIP")
            # print("[INFO]: THERE ARE {} ENTRIES IN FORM DATA".format(len(current_job)))
            # Store to Database
            # this_job = NormalJobsModel(*current_job)
            # print(this_job)

            if len(current_job.keys()) == 12:
                # Add start_date, end_date, meet_and_greet, flight_details, special_requiremetns as nulls
                pass
        
        return "[INFO]: THERE ARE {} ENTRIES IN FORM DATA".format(len(current_job))

    return {"message" : "The request method not found, it should only be 'GET' or 'POST' ", "status" : 404}

# Get all jobs for this comapny only
@app.route('/search-jobs')
@app.route('/<string:company>/')
def search_jobs(company = None):
    if company: 
        return company + " JOBS LIST"
    else: 
        return render_template('list.html')

# Update Job (Retrieve Edit Form & Handle the Post request from Edit Form)
@app.route('/<int:id>/<string:type>/edit', methods=['POST', 'GET'])
def update(id = None, type = None):
    return "UPDATE REQUEST"

# Delete a job from a table based on job id
@app.route('/<int:id>/<string:type>/delete')
def delete(id = None, type = None):
    if id and type:
        return "DELETE REQUEST FOR JOB WITH ID : {} and TYPE: {}".format(id, type)

if __name__ == "__main__":
    logger.debug("Starting app service...")
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)