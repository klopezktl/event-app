from flask import Flask, request

app = Flask(__name__)

events = [
    {
        "event_code": "my_event_1",
        "event_name": "My event 1",
        "start_date": "2023-01-01",
        "end_date": "2023-01-05"
    },
    {
        "event_code": "my_event_2",
        "event_name": "My event 2",
        "start_date": "2023-01-06",
        "end_date": "2023-01-07"
    }
]

# List
@app.get("/event")
def get_events():
    return {"events": events}

# Create
@app.post("/event")
def create_event():
    request_data = request.get_json()
    new_event = {
        "event_code": request_data['event_code'],
        "event_name": request_data["event_name"],
        "start_date": request_data["start_date"],
        "end_date": request_data["end_date"]
    }

    events.append(new_event)
    return new_event, 201

# Update
@app.put("/event/<string:event_code>")
def update_event(event_code):
    request_data = request.get_json()
    for event in events:
        if event['event_code'] == event_code:
            event['event_name'] = request_data['event_name']
            event['start_date'] = request_data['start_date']
            event['end_date'] = request_data['end_date']

    return events, 201

# Delete
@app.post("/event/<string:event_code>")
def delete_event(event_code):
    for i in range(len(events)):
        if events[i]['event_code'] == event_code:
            del events[i]
            break

    return events, 201