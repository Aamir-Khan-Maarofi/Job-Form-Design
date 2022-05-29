from pprint import pprint
from google_apis import convert_to_RFC_datetime, create_service

API_VERSION = "V3"
API_NAME = "calendar"
CLIENT_SECRET_FILE = "./credentials.json"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = "7u0t8lmtiuacd8bgkcihphsauo@group.calendar.google.com"

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def event_data(s_date, p_time, r_time=None, e_date=None):
    timezone_offset = 5
    s_date = s_date.split('-')
    year, month, day = int(s_date[-3]), int(s_date[-2]), int(s_date[-1])

    p_time = [time.strip() for time in p_time.split(":")]
    p_hour = int(p_time[0])
    p_minutes, p_period = p_time[1].split(" ")
    
    if p_period == "PM" and p_hour < 12:
        p_hour = p_hour + 12
    elif p_period == "PM" and p_hour == 12:
        p_hour = 00

    if p_hour < timezone_offset:
        p_start_hour = 24 + (p_hour - timezone_offset)
        p_end_hour = 24 + (p_hour - timezone_offset + 2)
        day = day - 1
    else:
        p_start_hour = p_hour - timezone_offset
        p_end_hour = p_hour - timezone_offset + 2

    data = {
        "year" : year,
        "month" : month, 
        "p_day" : day, 
        "p_start_hour" : p_start_hour, 
        "p_end_hour" : p_end_hour, 
        "p_minute" : int(p_minutes)
    }

    if r_time: 
        r_day = int(s_date[-1])
        r_time = [time.strip() for time in r_time.split(":")]
        r_hour = int(r_time[0])
        r_minutes, r_period = r_time[1].split(" ")
        
        if r_period == "PM" and r_hour < 12:
            r_hour = r_hour + 12
        elif r_period == "PM" and r_hour == 12:
            r_hour = 00

        if r_hour < timezone_offset:
            r_start_hour = 24 + (r_hour - timezone_offset)
            r_end_hour = 24 + (r_hour - timezone_offset + 2)
            r_day = r_day - 1
        else:
            r_start_hour = r_hour - timezone_offset
            r_end_hour = r_hour - timezone_offset + 2

        data['r_start_hour'] = r_start_hour
        data['r_end_hour'] = r_end_hour
        data['r_minute'] = int(r_minutes)
        data['r_day'] = r_day
    
    if e_date:
        e_date = e_date.split('-')
        data['rec_count'] = int(e_date[-1]) - int(s_date[-1]) + 1
    pprint(data)
    return data

# Create Events on create request


def create_event(job_type, start_date=None, end_date=None, pickup_time=None, return_time=None):
    timezone = 'Asia/PKT'
    if job_type and job_type == "NORMAL_JOB":
        # If the current job has only start time then create one event for two hours starting at start time
        if pickup_time and not return_time:
            data = event_data(start_date, pickup_time)
            body = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['p_day'], data['p_start_hour'], data['p_minute']),
                    'timezone': timezone,
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['p_day'], data['p_end_hour'], data['p_minute']),
                    'timezone': timezone,
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
            pprint(response)
            print("Created one event for the date")

            # NOTE : Exit from here with the calendar id
            return {
                "pickup_id" : response['id']
            }

        # If the current job has both start/return time then create two events each 2 hours long
        if pickup_time and return_time:
            data = event_data(start_date, pickup_time, return_time)
            pprint(data)
            pickup_body = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['p_day'], data['p_start_hour'], data['p_minute']),
                    'timezone': 'Asia/PKT',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['p_day'], data['p_end_hour'], data['p_minute']),
                    'timezone': 'Asia/PKT',
                },

                'summary': 'NORMAL JOB - Pickup Event',
                'description': 'This automated event was created from python script, if this works then say BOOM!',
                'status': 'confirmed',
                'visibility': 'public',
            }

            return_body = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['r_day'], data['r_start_hour'], data['r_minute']),
                    'timezone': 'Asia/PKT',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['r_day'], data['r_end_hour'], data['r_minute']),
                    'timezone': 'Asia/PKT',
                },

                'summary': 'NORMAL Job - Return Event',
                'description': 'This automated event was created from python script, if this works then say BOOM!',
                'status': 'confirmed',
                'visibility': 'public',
            }

            pickup_response = service.events().insert(
                calendarId=CALENDAR_ID,
                body=pickup_body
            ).execute()

            return_response = service.events().insert(
                calendarId=CALENDAR_ID,
                body=return_body
            ).execute()

            pprint(pickup_response)
            pprint(return_response)
            print("Created two events for the date")
            
            return {
                "pickup_id" : pickup_response['id'],
                "return_id" : return_response['id']
            }
        
    if job_type and job_type == "DAILY_JOB":
        # if the current job has only start time then create one event for all dates (start - end dates both inclusive) each two hours long
        if pickup_time and not return_time:
            data = event_data(start_date, pickup_time, e_date=end_date)

            body = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['p_day'], data['p_start_hour'], data['p_minute']),
                    'timeZone': 'Asia/Karachi',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['p_day'], data['p_end_hour'], data['p_minute']),
                    'timeZone': 'Asia/Karachi',
                },

                'recurrence': [
                    'RRULE:FREQ=DAILY;INTERVAL=1;COUNT={}'.format(data['rec_count'])
                ],

                'summary': 'Daily Job One Event - Two hours long  - till end date',
                'description': 'This automated event was created from python script, if this works then say BOOM!',
                'status': 'confirmed',
                'visibility': 'public',
            }

            response = service.events().insert(
                calendarId=CALENDAR_ID,
                body=body
            ).execute()

            print("Created one event for all days in range")
            return {
                'pickup_id' : response['id']
            }
        # If the current job has both start/return times then create two events per day for all dates (both start/end times inclusive)
        if pickup_time and return_time:
            data = event_data(start_date, pickup_time, return_time, end_date)

            pickup_body = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['p_day'], data['p_start_hour'], data['p_minute']),
                    'timeZone': 'Asia/Karachi',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['p_day'], data['p_end_hour'], data['p_minute']),
                    'timeZone': 'Asia/Karachi',
                },

                'recurrence': [
                    'RRULE:FREQ=DAILY;INTERVAL=1;COUNT={}'.format(data['rec_count'])
                ],

                'summary': 'Daily Job PICKUP Event - Two hours long  - till end date',
                'description': 'This automated event was created from python script, if this works then say BOOM!',
                'status': 'confirmed',
                'visibility': 'public',
            }

            return_body = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['r_day'], data['r_start_hour'], data['r_minute']),
                    'timeZone': 'Asia/Karachi',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(data['year'], data['month'], data['r_day'], data['r_end_hour'], data['r_minute']),
                    'timeZone': 'Asia/Karachi',
                },

                'recurrence': [
                    'RRULE:FREQ=DAILY;INTERVAL=1;COUNT={}'.format(data['rec_count'])
                ],

                'summary': 'Daily Job RETURN Event - Two hours long  - till end date',
                'description': 'This automated event was created from python script, if this works then say BOOM!',
                'status': 'confirmed',
                'visibility': 'public',
            }

            pickup_response = service.events().insert(
                calendarId=CALENDAR_ID,
                body=pickup_body
            ).execute()

            return_response = service.events().insert(
                calendarId=CALENDAR_ID,
                body=return_body
            ).execute()

            print("Created two events per day for all days in range")
            
            return {
                "pickup_id" : pickup_response['id'],
                "return_id" : return_response['id']
            }

        print("Create Recurrent Event for mentioned dates")


# edit event on edit request
def edit_events(job_type, event_ids, start_date=None, end_date=None, pickup_time=None, return_time=None):
    if job_type and job_type == "NORMAL_JOB":
        if len(event_ids) == 1:
            date = start_date.split('-')
            # time = pickup_time.split(':')

            pickup_time = [time.strip() for time in pickup_time.split(":")]
            pickup_hours = int(pickup_time[0])
            pickup_minutes, pickup_period = pickup_time[1].split(" ")
            if pickup_period == "PM" and pickup_hours < 12:
                pickup_hours = pickup_hours + 12
            elif pickup_period == "PM" and pickup_hours == 12:
                pickup_hours = 00

            body = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-3]),
                        int(date[-2]),
                        int(date[-1]),
                        int(pickup_hours),
                        int(pickup_minutes)
                    ),
                    'timezone': 'Asia/PKT',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-3]),
                        int(date[-2]),
                        int(date[-1]),
                        int(pickup_hours)+2,
                        int(pickup_minutes)
                    ),
                    'timezone': 'Asia/PKT',
                },

                'summary': 'Normal Job One Event - Two hours long',
                'description': 'This automated event was created from python script, if this works then say BOOM!',
                'status': 'confirmed',
                'visibility': 'public',
            }

            event = service.events().get(calendarId=CALENDAR_ID,eventId=event_ids[0]).execute()
            updated_event = service.events().update(calendarId=CALENDAR_ID, eventId=event['id'], body=body).execute()
            pprint(updated_event)
            print("UPDATED...")
        else:
            date = start_date.split('-')

            pickup_time = [time.strip() for time in pickup_time.split(":")]
            pickup_hours = int(pickup_time[0])
            pickup_minutes, pickup_period = pickup_time[1].split(" ")
            if pickup_period == "PM" and pickup_hours < 12:
                pickup_hours = pickup_hours + 12
            elif pickup_period == "PM" and pickup_hours == 12:
                pickup_hours = 00

            return_time = [time.strip() for time in return_time.split(":")]
            return_hours = int(return_time[0])
            return_minutes, return_period = return_time[1].split(" ")
            if return_period == "PM" and return_hours < 12:
                return_hours = return_hours + 12
            elif return_period == "PM" and return_hours == 12:
                return_hours = 00

            body_pickup = {
                'start': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-3]),
                        int(date[-2]),
                        int(date[-1]),
                        int(pickup_hours),
                        int(pickup_minutes)
                    ),
                    'timezone': 'Asia/PKT',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-3]),
                        int(date[-2]),
                        int(date[-1]),
                        int(pickup_hours),
                        int(pickup_minutes)
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
                        int(date[-3]),
                        int(date[-2]),
                        int(date[-1]),
                        int(return_hours),
                        int(return_minutes)
                    ),
                    'timezone': 'Asia/PKT',
                },

                'end': {
                    'dateTime': convert_to_RFC_datetime(
                        int(date[-3]),
                        int(date[-2]),
                        int(date[-1]),
                        int(return_hours),
                        int(return_minutes)
                    ),
                    'timezone': 'Asia/PKT',
                },

                'summary': 'NORMAL Job - Return Event',
                'description': 'This automated event was created from python script, if this works then say BOOM!',
                'status': 'confirmed',
                'visibility': 'public',
            }

            pickup_event = service.events().get(calendarId=CALENDAR_ID,
                                                eventId=event_ids[0]).execute()
            return_event = service.events().get(calendarId=CALENDAR_ID,
                                                eventId=event_ids[1]).execute()
            updated_pickup_event = service.events().update(
                calendarId=CALENDAR_ID, eventId=pickup_event['id'], body=body_pickup).execute()
            updated_return_event = service.events().update(
                calendarId=CALENDAR_ID, eventId=return_event['id'], body=body_return).execute()
        # Get the existing event
        # Update it with new data
        print("Updated event for normal job")
    if job_type and job_type == "DAILY_JOB":
        if len(event_ids) == 1:
            pass
        else:
            pass
        # Get the existing multidays recurrent event
        # Update it with new data
        print("Updated event for daily jobs")


def delete_events(job_type, event_ids):
    if job_type and job_type == "NORMAL_JOB":
        print("Deleted event(s) for normal job")
    if job_type and job_type == "DAILY_JOB":
        print("Deleted events for daily jobs")


if __name__ == "__main__":
    # create_event("NORMAL_JOB", start_date="2022-05-24", pickup_time='01 : 30 AM')
    # create_event("NORMAL_JOB", start_date="2022-05-22", pickup_time='10 : 30 AM', return_time='10 : 30 PM')
    # create_event("DAILY_JOB", start_date = "2022-05-24", end_date='2022-05-30', pickup_time='11 : 30 PM')
    create_event("DAILY_JOB", start_date = "2022-05-04", end_date="2022-05-15", pickup_time='10 : 30 AM', return_time='10 : 30 PM')

    # edit_events("NORMAL_JOB", ['aru4k2b5bup68kp7d5v7qi7amk'], start_date="2022-05-23", pickup_time="22:30")
    # edit_events("NORMAL_JOB", ['r7kt7nbao912pjk4jgp95trr98', '249bt9endgdsg313ikv8bjnmes'], start_date="2022-05-24", pickup_time="10:00", return_time="13:00")

    print("CALLED AS MAIN")
