from db import db
from sqlalchemy.sql import func

class EventModel(db.Model):
    __tablename__ = "app_events"

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(80), unique=True, nullable=False)
    start_date = db.Column(db.DateTime(), server_default=func.now())
    end_date = db.Column(db.DateTime(), server_default=func.now())