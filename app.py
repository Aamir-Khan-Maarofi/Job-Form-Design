from email.policy import default
from sqlite3 import Error
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

DB_NAME = app.root_path + "/jobs.db"


def get_company_jobs(company):
    cursor = sqlite3.connect(DB_NAME)

    daily_keys = ["id", "created_at", "company", "name", "billing_details", "job_priority", "type_of_trip", "client_details",
                  "pickup_date", "pickup_time", "return_time", "destination_details", "notes", "start_date", "end_date"]
    normal_keys = ["id", "created_at", "company", "name", "billing_details", "job_priority", "type_of_trip", "client_details",
                    "pickup_date", "pickup_time", "return_time", "destination_details", "notes", "job_type", "meet_greet",
                    "flight_details", "special_requirements"]

    companyJobs = []
    results = cursor.execute("SELECT * FROM DAILY_JOBS WHERE COMPANY IS '{}'".format(company))
    for result in results:
        companyJobs.append(dict(zip(daily_keys, result)))

    results = cursor.execute("SELECT * FROM NORMAL_JOBS WHERE COMPANY IS '{}'".format(company))
    for result in results:
        companyJobs.append(dict(zip(normal_keys, result)))

    cursor.close()
    return companyJobs

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jobs/create', methods=['POST'])
def create_new_job():
    # try:
    if request.method == "POST":
        cursor = sqlite3.connect(DB_NAME)
        response = dict(request.form)
        currentJob = [datetime.now().strftime("%d-%b-%Y %H:%M:%S:%f")]
        for value in response.values():
            currentJob.append(value)

        JOB_TYPE = "DAILY_JOBS" if response["type-of-trip"] == "daily-trips" else "NORMAL_JOBS"

        # if dailytrips:
        if JOB_TYPE == "DAILY_JOBS":
            print("It's a daily trip")

            # create multiple events one for a day (if return then create two events for the day)
            # if emergency, send Edwin the whatsap notification
            # Save entries to database and redirect user to list page
            ROW_STRING = \
                '''
                    INSERT INTO DAILY_JOBS (
                        JOB_CREATION_TIME, COMPANY, NAME, BILLING_DETAILS, JOB_PRIORITY, 
                        TYPE_OF_TRIP, CLIETN_DETAILS, PICkUP_DATE, PICKUP_TIME, RETURN_TIME, 
                        DESTINATION_DETAILS, NOTES, START_DATE, END_DATE
                    )

                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                '''

            cursor.execute(ROW_STRING, currentJob)
            cursor.commit()

        # if normal trip:
        if JOB_TYPE == "NORMAL_JOBS":
            print("It's a Normal Trip")

            if response['job-type'] != "1":
                while(len(currentJob) < 16):
                    currentJob.append(None)

            # create one event for pickup date (if returnn then create two events)
            # if emergency send Edwin the whatsapp noticicaiton
            # Save entries to database and redirect user to list page
            ROW_STRING = \
                '''
                    INSERT INTO NORMAL_JOBS (
                        JOB_CREATION_TIME, COMPANY, NAME, BILLING_DETAILS, JOB_PRIORITY, TYPE_OF_TRIP,
                        CLIETN_DETAILS, PICkUP_DATE, PICKUP_TIME, RETURN_TIME, DESTINATION_DETAILS,
                        NOTES, JOB_TYPE, MEET_AND_GREET, FLIGHT_DETAILS, SPECIAL_REQUIREMENTS
                    )

                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                '''

            cursor.execute(ROW_STRING, currentJob)
            cursor.commit()
            cursor.close()
        
        company = currentJob[1]
        companyJobs = get_company_jobs(company)
        return render_template('list_jobs.html', jobs=companyJobs, title=company + " Jobs", company=company)

    # except Error as e:
    #     print(e)
    #     return "ERROR"

@app.route('/jobs/list')
@app.route('/jobs/list/<company>')
def list_jobs_for_company(company=None):
    # search database for
    jobs = get_company_jobs(company)
    if company and len(jobs):
        title = company + " Jobs"
    elif company and not len(jobs):
        title = "No Jobs Found For " + company
    else:
        title = ""
        company = "Please Enter Your Company Name"
    return render_template("list_jobs.html", jobs=jobs, title=title, company = company)


if __name__ == "__main__":
    app.run("localhost", port=5000)
