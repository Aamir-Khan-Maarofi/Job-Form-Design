import csv, os
from flask import Flask, render_template, request

app = Flask(__name__)

FILE_PATH = app.root_path + "/jobs.csv"
HEADERS = ['job-index', 'company', 'name', 'billing-details', 'job-priority', 'type-of-trip', 'client-details-etc',
        'pickup-date', 'pickup-timing', 'return-timing', 'destination-details', 'note',
        'start-date', 'end-date', 'job-type', 'Meet & Greet', 'flight-details', 'special-requirements']

def update_jobs(job):
    with open(FILE_PATH, mode='a', newline='') as jobs_file:
        writer = csv.writer(jobs_file)
        if os.stat(FILE_PATH).st_size == 0:
            print("[INFO] : APPEND HEADER & JOB")
            writer.writerow(HEADERS)
            writer.writerow(job)
        else:
            print("[INFO] : ONLY APPEND JOB")
            writer.writerow(job)

def get_serial():
    with open(FILE_PATH, mode='r') as jobs_file:
        # Get last row from the csv
        all_rows = list(csv.reader(jobs_file))
        print(list(all_rows))
        if len(all_rows) < 2:
            last_row = ['0']
        else:
            last_row = all_rows[-1]
    # Get latest serial number and return next serial number
    return int(last_row[0]) + 1

@app.route('/')
def index():
    return render_template('index.html')

# ['sno', 'company', 'name', 'billing-details', 'job-priority', 'type-of-trip', 'client-details-etc',
#  'pickup-date', 'pickup-timing', 'return-timing', 'destination-details', 'note',  
#  'start-date', 'end-date', 'job-type', 'Meet & Greet', 'flight-details', 'special-requirements']

@app.route('/jobs/create', methods=['POST'])
def create_new_job():
    if request.method == "POST":
        # Get Form Response and store it in database/sheet
        response = dict(request.form)
        keys, values = response.keys(), response.values()

        # if dailytrips:
        if response["type-of-trip"] == "daily-trips":
            print("It's a daily trip")
            # Add row entries from form to current job
            currentJob = [get_serial()]
            for value in response.values():
                currentJob.append(value)

            # create multiple events one for a day (if return then create two events for the day)
            # if emergency, send Edwin the whatsap notification
            # Save entries to database and redirect user to list page
        
        # if normal trip:
        if response["type-of-trip"] == "normal-trip":
            print("It's a Normal Trip")
            currentJob = [get_serial()]
            
            # see if arrival/departure:
            if response['job-type'] == "Arrival / Departure":
                for value in response.values():
                    currentJob.append(value)
            
                for index in [-4, -5]:
                    currentJob.insert(index, None)

                # create one event for pickup date (if returnn then create two events)
                # if emergency send Edwin the whatsapp noticicaiton
                # Save entries to database and redirect user to list page
            
            # if not arrival/departure:
            else:
                for value in response.values():
                    currentJob.append(value)
            
                for index in [-1, -1]:
                    currentJob.insert(index, None)

                # create one event for pickup date (if returnn then create two events)
                # if emergency send Edwin the whatsapp noticicaiton
                # Save entries to database and redirect user to list page
        
        update_jobs(currentJob)
        return "Done"


@app.route('/jobs/list/{user_email}')
def list_jobs_for_user(user_email):
    # search database for
    return "List of Jobs for current email address"


if __name__ == "__main__":
    app.run("localhost", port=5000)
