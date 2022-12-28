from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import EventSchema

from db import events
import uuid

blp = Blueprint("Events", __name__, description="Operations on events")

@blp.route("/event/<string:event_id>")
class Event(MethodView):

    @blp.arguments(EventSchema)
    @blp.response(200, EventSchema)
    def put(self, event_data, event_id):
        try:
            event = events[event_id]
            event |= event_data
            # event['event_name'] = event_data['event_name']
            # event['start_date'] = event_data['start_date']
            # event['end_date'] = event_data['end_date']
            return event
        except KeyError:
            abort(404, message="Event not found")

    def delete(self, event_id):
        try:
            del events[event_id]
            return events, 201
        except KeyError:
            abort(404, message="Event not found")

@blp.route("/event")
class EventList(MethodView):
    @blp.response(200, EventSchema(many=True))
    def get(self):
        return events.values()
        # return {"events": events}

    @blp.arguments(EventSchema)
    @blp.response(200, EventSchema)
    def post(self, event_data):
        event_id = uuid.uuid4().hex
        event = {**event_data, "id": event_id}
        events[event_id] = event
        return event, 201




