from flask import Flask, request
from flask_smorest import abort
from db import events
import uuid

app = Flask(__name__)

# List
@app.get("/event")
def get_events():
    # return {"events": list(events.values())}
    return {"events": events}

# Create
@app.post("/event")
def create_event():
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

# Update
@app.put("/event/<string:event_id>")
def update_event(event_id):
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

# Delete
@app.delete("/event/<string:event_id>")
def delete_event(event_id):
    try:
        del events[event_id]
        return events, 201
    except KeyError:
        abort(404, message="Event not found")
