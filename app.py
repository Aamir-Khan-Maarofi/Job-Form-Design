from distutils.log import error
from sqlite3 import Error
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

DB_NAME = app.root_path + "/jobs.db"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jobs/create', methods=['POST'])
def create_new_job():
    try:
        if request.method == "POST":
            cursor = sqlite3.connect(DB_NAME)
            response = dict(request.form)
            currentJob = [datetime.now().strftime("%d-%b-%Y %H:%M:%S:%f")]
            for value in response.values():
                currentJob.append(value)
        
            # if dailytrips:
            if response["type-of-trip"] == "daily-trips":
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
                cursor.close()
            
            # if normal trip:
            if response["type-of-trip"] == "normal-trip":
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

            return render_template('list_jobs.html')

    except Error as e:
        print(e)
        return "ERROR"

@app.route('/jobs/list/{user_email}')
def list_jobs_for_user(user_email):
    # search database for
    return "List of Jobs for current email address"


if __name__ == "__main__":
    app.run("localhost", port=5000)
