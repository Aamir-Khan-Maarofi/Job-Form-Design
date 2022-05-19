#########################################################################
############################# TEST CODE #################################
#########################################################################

# hours_adjustment = 5
# body = {
#     'start' : {
#         'dateTime' : convert_to_RFC_datetime(2022, 5, 20, 12 + hours_adjustment, 30),
#         'timezone' : 'Asia/PKT',
#     }, 

#     'end' : {
#         'dateTime' : convert_to_RFC_datetime(2022, 5, 20, 16 + hours_adjustment, 30),
#         'timezone' : 'Asia/PKT',
#     }, 

#     'summary' : 'Event From Python Script', 
#     'description' : 'This automated event was created from python script, if this works then say BOOM!',
#     'status' : 'confirmed', 
#     'visibility' : 'public', 

# }

# sendNotification = False
# sendUpdate = 'none'
# supportsAttachments = True

# response = service.events().insert(
#     calendarId = CALENDAR_ID, 
#     sendNotifications=sendNotification,
#     body=body
# ).execute()


# pprint(response)

#########################################################################
############################# TEST CODE #################################
#########################################################################


from pprint import pprint
from google_apis import convert_to_RFC_datetime, create_service

API_VERSION = "V3"
API_NAME = "calendar"
CLIENT_SECRET_FILE = "./credentials.json"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = "7u0t8lmtiuacd8bgkcihphsauo@group.calendar.google.com"

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Create Events on create request
def create_event(job_type):
    if job_type and job_type == "NORMAL_JOB":
        # If the current job has only start time then create one event for two hours starting at start time 
        # If the current job has both start/return time then create two events each 2 hours long
        
        # Take in cosideration the overlapping timings in two dates (e.g. 10:01 PM - 12:01 AM and 11:59 PM - 01:59 AM)
        # Take in consideration the timezone and GMT hours (to be added or subtracted)
        print("Create One Time Event")
    if job_type and job_type == "DAILY_JOB":
        # if the current job has only start time then create one event for all dates (start - end dates both inclusive) each two hours long
        # If the current job has both start/return times then create two events per day for all dates (both start/end times inclusive)

        # Take in cosideration the overlapping timings in two dates (e.g. 10:01 PM - 12:01 AM and 11:59 PM - 01:59 AM)
        # Take in consideration the timezone and GMT hours (to be added or subtracted)
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