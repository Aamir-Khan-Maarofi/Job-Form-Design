from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs/create', methods=['POST'])
def create_new_job():
    if request.method == "POST":
        # Get Form Response and store it in database/sheet
        response = dict(request.form)
        keys, values = response.keys(), response.values()
        print(keys)
        print(values)
        print(response["view"])

        # if dailytrips:
        if response["view"] == "daily-trips":
            print("It's a daily trip")
            # get the start and end date

        #    create multiple events one for a day (if return then create two events for the day)
        #    if emergency, send Edwin the whatsap notification
        #    Save entries to database and redirect user to list page
        # if normal trip:
        if response["view"] == "normal-trip":
            print("It's a Normal Trip")
        #    see if arrival/departure:
        #       get the thre more questions
        #       create one event for pickup date (if returnn then create two events)
        #       if emergency send Edwin the whatsapp noticicaiton
        #       Save entries to database and redirect user to list page
        #   if not arrival/departure:
        #       do not get three questions
        #       create one event for pickup date (if returnn then create two events)
        #       if emergency send Edwin the whatsapp noticicaiton
        #       Save entries to database and redirect user to list page
        
        return "Done"

@app.route('/jobs/list/{user_email}')
def list_jobs_for_user(user_email):
    # search database for 
    return "List of Jobs for current email address"

if __name__ == "__main__":
    app.run("localhost", port=5000)