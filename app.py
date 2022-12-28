from flask import Flask, request
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
    event_id = uuid.uuid4().hex
    event = {**event_data, "id": event_id}
    events[event_id] = event
    return event, 201

# Update
@app.put("/event/<string:event_id>")
def update_event(event_id):
    request_data = request.get_json()
    if event_id not in events:
        return {"message": "Event not found"}, 404

    event = events.get(event_id)
    event['event_name'] = request_data['event_name']
    event['start_date'] = request_data['start_date']
    event['end_date'] = request_data['end_date']

    return event, 201

# Delete
@app.post("/event/<string:event_id>")
def delete_event(event_id):
    try:
        del events[event_id]
        return events, 201
    except KeyError:
        return {"message": "Event not found"}, 404
