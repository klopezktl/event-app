from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import EventModel
from schemas import EventSchema

from datetime import datetime

from sqlalchemy.dialects import sqlite
from sqlalchemy import and_

import uuid


blp = Blueprint("Events", __name__, description="Operations on events")
MIN_TIME = "8:00"
MAX_TIME = "16:00"

@blp.route("/event/<string:event_id>")
class Event(MethodView):

    @blp.arguments(EventSchema)
    @blp.response(200, EventSchema)
    def put(self, event_data, event_id):
        event = EventModel.query.get(event_id)

        # Validate start_date and end_date
        datetime_validations(event_data['start_date'], event_data['end_date'])

        if event:
            event.event_name = event_data['event_name']
            event.start_date = event_data['start_date']
            event.end_date = event_data['end_date']
        else:
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
    min_time = datetime.strptime(MIN_TIME, "%H:%M")
    min_time = min_time.time()

    max_time = datetime.strptime(MAX_TIME, "%H:%M")
    max_time = max_time.time()

    current_time = date_time.time()

    return min_time <= current_time <= max_time

def check_if_past_date(date_time):
    date_now = datetime.now()

    return True if date_time <= date_now else False

def datetime_validations(start_date, end_date):
    if not check_if_past_date(start_date) or not check_if_past_date(end_date):
        abort(
            400,
            message="Invalid start_date or end_date"
        )
    elif not check_if_time_in_range(start_date) or not check_if_time_in_range(end_date):
        abort(
            400,
            message="Event start_date or end_date is not within range"
        )
    else:
        check_overlap = EventModel.query.filter(
            EventModel.start_date.between(str(start_date), str(end_date))
        ).first()
        if check_overlap is not None:
            abort(
                400,
                message="Overlapping start_date or end_date"
            )





