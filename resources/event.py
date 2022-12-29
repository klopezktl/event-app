from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import EventModel
from schemas import EventSchema
from utils.contants.event import MIN_TIME, MAX_TIME, DATETIME_FORMAT, TIME_FORMAT

from datetime import datetime

blp = Blueprint("Events", __name__, description="Operations on events")

@blp.route("/event/<string:event_id>")
class Event(MethodView):

    @blp.response(200, EventSchema)
    def get(self, event_id):
        event = EventModel.query.get_or_404(event_id)
        return event

    @blp.arguments(EventSchema)
    @blp.response(200, EventSchema)
    def put(self, event_data, event_id):
        event = EventModel.query.get(event_id)

        # Validate start_date and end_date
        datetime_validations(event_data['start_date'], event_data['end_date'])

        if event:
            # Update
            event.event_name = event_data['event_name']
            event.start_date = event_data['start_date']
            event.end_date = event_data['end_date']
        else:
            # Insert
            event = EventModel(id=event_id, **event_data)

        db.session.add(event)
        db.session.commit()

        return event

    def delete(self, event_id):
        event = EventModel.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        return {"message": "Event is deleted."}, 200

@blp.route("/event")
class EventList(MethodView):
    @blp.response(200, EventSchema(many=True))
    def get(self):
        return EventModel.query.all()

    @blp.arguments(EventSchema)
    @blp.response(200, EventSchema)
    def post(self, event_data):
        event = EventModel(**event_data)

        # Validate start_date and end_date
        datetime_validations(event.start_date, event.end_date)

        try:
            db.session.add(event)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="An event with that name already exist"
            )
        except SQLAlchemyError:
            abort(500, message="An error occured while inserting event")

        return event, 201

def check_if_time_in_range(date_time):
    min_time = datetime.strptime(MIN_TIME, TIME_FORMAT)
    min_time = min_time.time()

    max_time = datetime.strptime(MAX_TIME, TIME_FORMAT)
    max_time = max_time.time()

    current_time = datetime.strptime(date_time, DATETIME_FORMAT)
    current_time = current_time.time()

    return min_time <= current_time <= max_time

def check_if_future_date(date_time):
    date_now = datetime.now()
    date_time = datetime.strptime(date_time, DATETIME_FORMAT)

    return True if date_time >= date_now else False

def datetime_validations(start_date, end_date):
    start_date = start_date.strftime(DATETIME_FORMAT)
    end_date = end_date.strftime(DATETIME_FORMAT)
    if not check_if_future_date(start_date) or not check_if_future_date(end_date):
        abort(
            400,
            message="Invalid start_date or end_date. Must be future date."
        )
    elif not check_if_time_in_range(start_date) or not check_if_time_in_range(end_date):
        abort(
            400,
            message="Event start_date or end_date is not within range."
        )
    else:
        query = EventModel.query.filter(
            EventModel.start_date.between(str(start_date), str(end_date))
        )
        check_overlap = query.first()
        if check_overlap is not None:
            abort(
                400,
                message="Overlapping start_date or end_date."
            )





