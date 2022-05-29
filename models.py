import datetime
import logging as logger
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
logger.basicConfig(level="DEBUG")


class JobsModel(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    company = db.Column(db.String())
    name = db.Column(db.String())
    billing_details = db.Column(db.Text())
    priority = db.Column(db.String())
    trip_type = db.Column(db.String())
    clients_details = db.Column(db.Text())
    pickup_date = db.Column(db.Date())
    pickup_time = db.Column(db.Time())
    return_time = db.Column(db.Time())
    destination = db.Column(db.Text())
    notes = db.Column(db.Text())
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())
    job_type = db.Column(db.String())
    meet_greet = db.Column(db.String())
    flight_details = db.Column(db.String())
    special_requirements = db.Column(db.String())
    pickup_event_id = db.Column(db.String())
    return_event_id = db.Column(db.String())

    def __init__(self, data) -> None:

        logger.debug("Createing new job instance...")

        self.company = data['company']
        self.name = data['name']
        self.billing_details = data['billing_details']
        self.priority = data['priority']
        self.trip_type = data['trip_type']
        self.clients_details = data['clients_details']
        self.pickup_date = data['pickup_date']
        self.pickup_time = data['pickup_time']
        self.return_time = data['return_time']
        self.destination = data['destination']
        self.notes = data['notes']
        self.start_date = data['start_date']
        self.end_date = data['end_date']
        self.job_type = data['job_type']
        self.meet_greet = data['meet_greet']
        self.flight_details = data['flight_details']
        self.special_requirements = data['special_requirements']
        self.pickup_event_id = data['pickup_event_id']
        self.return_event_id = data['return_event_id']
        
        logger.debug("Created new job instance...")

    def __repr__(self) -> str:
        return "{}, {}, {}, {}, {}".format(self.pickup_date, self.pickup_time, self.return_time, self.name, self.clients_details)
























# class DailyJobsModel(db.Model):
#     __tablename__ = "daily_jobs"

#     id = db.Column(db.Integer, primary_key=True)
#     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
#     company = db.Column(db.String())
#     name = db.Column(db.String())
#     billing_details = db.Column(db.Text())
#     priority = db.Column(db.String())
#     trip_type = db.Column(db.String())
#     clients_details = db.Column(db.Text())
#     pickup_date = db.Column(db.Date())
#     pickup_time = db.Column(db.Time())
#     return_time = db.Column(db.Time())
#     destination = db.Column(db.Text())
#     notes = db.Column(db.Text())
#     start_date = db.Column(db.Date())
#     end_date = db.Column(db.Date())

#     def __init__(self, company, name, billing_details, priority, trip_type,
#                  clients_details, pickup_date, pickup_time, return_time,
#                  destination, notes, start_date, end_date) -> None:

#         logger.debug("Createing new daily job instance...")

#         self.company = company
#         self.name = name
#         self.billing_details = billing_details
#         self.priority = priority
#         self.trip_type = trip_type
#         self.clients_details = clients_details
#         self.pickup_date = pickup_date
#         self.pickup_time = pickup_time
#         self.return_time = return_time
#         self.destination = destination
#         self.notes = notes
#         self.start_date = start_date
#         self.end_date = end_date

#         logger.debug("Created new daily job instance...")

#     def __repr__(self) -> str:
#         return "{}, {}, {}, {}, {}".format(self.company, self.trip_type, self.id, self.name, self.clients_details)


# class NormalJobsModel(db.Model):
#     __tablename__ = "normal_jobs"

#     id = db.Column(db.Integer(), primary_key=True)
#     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
#     company = db.Column(db.String())
#     name = db.Column(db.String())
#     billing_details = db.Column(db.Text())
#     priority = db.Column(db.String())
#     trip_type = db.Column(db.String())
#     clients_details = db.Column(db.Text())
#     pickup_date = db.Column(db.Date())
#     pickup_time = db.Column(db.Time())
#     return_time = db.Column(db.Time())
#     destination = db.Column(db.Text())
#     notes = db.Column(db.Text())
#     job_type = db.Column(db.String())
#     meet_greet = db.Column(db.String())
#     flight_details = db.Column(db.String())
#     special_requirements = db.Column(db.String())

#     def __init__(self, company, name, billing_details, priority, trip_type,
#                  clients_details, pickup_date, pickup_time, return_time, destination,
#                  notes, job_type, meet_greet, flight_details, special_requirements) -> None:

#         logger.debug("Createing new normal job instance...")

#         self.company = company
#         self.name = name
#         self.billing_details = billing_details
#         self.priority = priority
#         self.trip_type = trip_type
#         self.clients_details = clients_details
#         self.pickup_date = pickup_date
#         self.pickup_time = pickup_time
#         self.return_time = return_time
#         self.destination = destination
#         self.notes = notes
#         self.job_type = job_type
#         self.meet_greet = meet_greet
#         self.flight_details = flight_details
#         self.special_requirements = special_requirements

#         logger.debug("Created new normal job instance...")

#     def __repr__(self) -> str:
#         return "{}, {}, {}, {}, {}".format(self.company, self.trip_type, self.id, self.name, self.clients_details)
