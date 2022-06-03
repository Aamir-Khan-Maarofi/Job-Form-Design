import logging as logger
from datetime import datetime
from pprint import pprint
from google_calendar import create_event
from models import db, JobsModel
from flask import Flask, redirect, render_template, request
logger.basicConfig(level="DEBUG")

app = Flask(__name__)
db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Create object based on provided data
def create_job_object(current_job, job_type, event_ids, flag='create'):
    data = dict()
    if event_ids:
        if len(event_ids) == 2:
            data['pickup_event_id'] = event_ids['pickup_event_id']
            data['return_event_id'] = event_ids['return_event_id']
        else:
            data['pickup_event_id'] = event_ids['pickup_event_id']
            data['return_event_id'] = None

    if job_type == "DAILY_JOB":
        print("[INFO: IT'S A DAILY TRIP]")

        data['company'] = current_job['company']
        data['name'] = current_job['name']
        data['billing_details'] = current_job['billing-details']
        data['priority'] = current_job['job-priority']
        data['trip_type'] = current_job['type-of-trip']
        data['clients_details'] = current_job['client-details-etc']
        data['pickup_date'] = datetime.strptime(current_job['pickup-date'], "%Y-%m-%d")

        data['pickup_time'] = datetime.strptime(current_job['pickup-timing'], "%I : %M %p").time()
        if 'return-timing' in current_job.keys():
            data['return_time'] = datetime.strptime(current_job['return-timing'], "%I : %M %p").time()
        else:
            data['return_time'] = None

        data['destination'] = current_job['destination-details']
        data['notes'] = current_job['note']
        data['start_date'] = datetime.strptime(current_job['start-date'], "%Y-%m-%d")
        data['end_date'] = datetime.strptime(current_job['end-date'], "%Y-%m-%d")
        data['job_type'] = None
        data['meet_greet'] = None
        data['flight_details'] = None
        data['special_requirements'] = None
    
    if job_type == "NORMAL_JOB":
        print("[INFO]: IT'S A NORMAL TRIP")

        data['company'] = current_job['company']
        data['name'] = current_job['name']
        data['billing_details'] = current_job['billing-details']
        data['priority'] = current_job['job-priority']
        data['trip_type'] = current_job['type-of-trip']
        data['clients_details'] = current_job['client-details-etc']
        data['pickup_date'] = datetime.strptime(current_job['pickup-date'], "%Y-%m-%d")

        data['pickup_time'] = datetime.strptime(current_job['pickup-timing'], "%I : %M %p").time()
        if 'return-timing' in current_job.keys():
            data['return_time'] = datetime.strptime(current_job['return-timing'], "%I : %M %p").time()
        else:
            data['return_time'] = None

        data['destination'] = current_job['destination-details']
        data['notes'] = current_job['note']
        data['job_type'] = current_job['job-type']
        data['start_date'] = None
        data['end_date'] = None

        if not "Meet & Greet" in current_job.keys():
            data['meet_greet'] = None
            data['flight_details'] = None
            data['special_requirements'] = None

        else:
            data['meet_greet'] = current_job['Meet & Greet']
            data['flight_details'] = current_job['flight-details']
            data['special_requirements'] = current_job['special-requirements']
    
    pprint(data)
    return data


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
        pprint(current_job)
        job_type = "DAILY_JOB" if current_job['type-of-trip'] == "daily-trips" else "NORMAL_JOB"

        if job_type == "NORMAL_JOB":
            # create one event
            if 'return-timing' in current_job.keys():
                event_ids = create_event(
                    job_type=job_type, 
                    start_date=current_job['pickup-date'], 
                    pickup_time=current_job['pickup-timing'],
                    return_time=current_job['return-timing'], 
                )
            else: 
                event_ids = create_event(
                    job_type=job_type, 
                    start_date=current_job['pickup-date'], 
                    pickup_time=current_job['pickup-timing'],
                )
            
        else:
            # create multiple events
            print("DAILY JOB .......................")
            if 'return-timing' in current_job.keys():
                event_ids = create_event(
                    job_type=job_type, 
                    start_date=current_job['start-date'], 
                    end_date=current_job['end-date'],
                    pickup_time=current_job['pickup-timing'],
                    return_time=current_job['return-timing'], 
                )
            else:
                event_ids = create_event(
                    job_type=job_type, 
                    start_date=current_job['start-date'], 
                    end_date=current_job['end-date'],
                    pickup_time=current_job['pickup-timing'],
                )

        data = create_job_object(current_job, job_type, event_ids)
        job = JobsModel(data=data)
        db.session.add(job)
        db.session.commit()

        # If job is immediate send whatsapp invite.

        return redirect('/{}'.format(job.company))

    return {"message": "The request method not found, it should only be 'GET' or 'POST' ", "status": 404}

# Get all jobs for this comapny only


@app.route('/search-jobs')
@app.route('/<string:company>/')
def search_jobs(company=None):
    if company:
        jobs = db.session.query(JobsModel).filter(
            JobsModel.company == company).all()
        return render_template('list.html', jobs=jobs)
    else:
        return render_template('list.html')

# Update Job (Retrieve Edit Form & Handle the Post request from Edit Form)


@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def update(id=None):
    if request.method == "GET":
        job = db.session.query(JobsModel).filter(JobsModel.id == id).first()
        print(job)
        return render_template('update.html', job=job)
    elif request.method == "POST":
        edit_job = dict(request.form)
        job = db.session.query(JobsModel).filter(JobsModel.id == edit_job['id']).first()
        job_type = "DAILY_JOB" if edit_job['type-of-trip'] == "daily-trips" else "NORMAL_JOB"

        data = create_job_object(edit_job, job_type, None, 'update')
        db.session.query(JobsModel).filter(JobsModel.id == edit_job['id']).update(data)
        db.session.commit()

        if job_type == "NORMAL_JOB":
            # update one event
            pass
        else:
            # update multiple events
            pass

        # If job is immediate send whatsapp invite.

        return redirect('/{}'.format(job.company))
    return {"message": "The request method not found, it should only be 'GET' or 'POST' ", "status": 404}

# Delete a job from a table based on job id


@app.route('/<int:id>/delete')
def delete(id=None):
    if id:
        try:
            job = db.session.query(JobsModel).filter(JobsModel.id == id).first()
            db.session.query(JobsModel).filter(JobsModel.id == id).delete()
            db.session.commit()

            return redirect('/{}'.format(job.company))
        except: 
            return {"message" : "Error occured during deletion of the Job", "status": 404}
            
    return {"message": "No Id is supplied for the job to be deleted. ", "status": 404} 


if __name__ == "__main__":
    logger.debug("Starting app service...")
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
