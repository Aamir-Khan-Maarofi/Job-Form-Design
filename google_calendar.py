from datetime import date
from pprint import pprint
from google_apis import convert_to_RFC_datetime, create_service

API_VERSION = "V3"
API_NAME = "calendar"
CLIENT_SECRET_FILE = "./credentials.json"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = "7u0t8lmtiuacd8bgkcihphsauo@group.calendar.google.com"

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Create Events on create request


def create_event(job_type, start_date=None, end_date=None, pickup_time=None, return_time=None):
    if job_type and job_type == "NORMAL_JOB":
        # If the current job has only start time then create one event for two hours starting at start time
        if pickup_time and not return_time:
            date = start_date.split('/')
            time = pickup_time.split(':')
            body = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-1]),
                        int(date[-2]),
                        int(date[-3]),
                        int(time[0])-5,
                        int(time[1])
                    ),
                    'timezone': 'Asia/PKT',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-1]),
                        int(date[-2]),
                        int(date[-3]),
                        int(time[0])-5+2,
                        int(time[1])
                    ),
                    'timezone': 'Asia/PKT',
                },

                'summary': 'Normal Job One Event - Two hours long',
                'description': 'This automated event was created from python script, if this works then say BOOM!',
                'status': 'confirmed',
                'visibility': 'public',
            }
            response = service.events().insert(
                calendarId=CALENDAR_ID,
                body=body
            ).execute()

            print("Created one event for the date")
        # If the current job has both start/return time then create two events each 2 hours long
        if pickup_time and return_time:
            date = start_date.split('/')
            pickup_time = pickup_time.split(':')
            return_time = return_time.split(':')

            body_pickup = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-1]),
                        int(date[-2]),
                        int(date[-3]),
                        int(pickup_time[0])-5,
                        int(pickup_time[1])
                    ),
                    'timezone': 'Asia/PKT',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-1]),
                        int(date[-2]),
                        int(date[-3]),
                        int(pickup_time[0])-5+2,
                        int(pickup_time[1])
                    ),
                    'timezone': 'Asia/PKT',
                },

                'summary': 'NORMAL JOB - Pickup Event',
                'description': 'This automated event was created from python script, if this works then say BOOM!',
                'status': 'confirmed',
                'visibility': 'public',
            }

            body_return = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-1]),
                        int(date[-2]),
                        int(date[-3]),
                        int(return_time[0])-5,
                        int(return_time[1])
                    ),
                    'timezone': 'Asia/PKT',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-1]),
                        int(date[-2]),
                        int(date[-3]),
                        int(return_time[0])-5+2,
                        int(return_time[1])
                    ),
                    'timezone': 'Asia/PKT',
                },

                'summary': 'NORMAL Job - Return Event',
                'description': 'This automated event was created from python script, if this works then say BOOM!',
                'status': 'confirmed',
                'visibility': 'public',
            }


            response_pickup = service.events().insert(
                calendarId=CALENDAR_ID,
                body=body_pickup
            ).execute()

            response_return = service.events().insert(
                calendarId=CALENDAR_ID,
                body=body_return
            ).execute()
            
            print("Created two events for the date")

        print("Create NORMAL JOB Event")
    if job_type and job_type == "DAILY_JOB":
        # if the current job has only start time then create one event for all dates (start - end dates both inclusive) each two hours long
        if pickup_time and not return_time:
            print("Created one event for all days in range")

        # If the current job has both start/return times then create two events per day for all dates (both start/end times inclusive)
        if pickup_time and return_time:
            print("Created two events per day for all days in range")

        print("Create Recurrent Event for mentioned dates")


# edit event on edit request
def edit_events(job_type):
    if job_type and job_type == "NORMAL_JOB":
        # Get the existing event
        # Update it with new data
        print("Updated event for normal job")
    if job_type and job_type == "DAILY_JOB":
        # Get the existing multidays recurrent event
        # Update it with new data
        print("Updated event for daily jobs")


if __name__ == "__main__":
    create_event("NORMAL_JOB", start_date = "22/05/2022", pickup_time="16:00", return_time="20:00")
    # create_event("NORMAL_JOB", start_date="22/05/2022", pickup_time="22:01")
    # create_event("DAILY_JOB", start_date = "22/05/2022", end_date="26/05/2022", pickup_time="16:00", return_time="20:00")
    # create_event("DAILY_JOB", start_date = "22/05/2022", end_date="26/05/2022", pickup_time="16:00")
