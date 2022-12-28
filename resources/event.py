from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import EventModel
from schemas import EventSchema

import uuid

blp = Blueprint("Events", __name__, description="Operations on events")

@blp.route("/event/<string:event_id>")
class Event(MethodView):

    @blp.arguments(EventSchema)
    @blp.response(200, EventSchema)
    def put(self, event_data, event_id):
        event = EventModel.query.get(event_id)
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




