from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView

from db import events
import uuid

blp = Blueprint("Events", __name__, description="Operations on events")

@blp.route("/event/<string:event_id>")
class Event(MethodView):
    def put(self, event_id):
        event_data = request.get_json()
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

    def get(self):
        # return {"events": list(events.values())}
        return {"events": events}

    def post(self):
        event_data = request.get_json()

        if(
            "event_name" not in event_data
            or "start_date" not in event_data
            or "end_date" not in event_data
        ):
            abort(
                400,
                message="Bad request."
            )
        else:
            event_id = uuid.uuid4().hex
            event = {**event_data, "id": event_id}
            events[event_id] = event
            return event, 201




