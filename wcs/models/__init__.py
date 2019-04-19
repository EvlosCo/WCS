import datetime
from wcs.database import db


class BaseModel(db.Model):
    id = db.Column(
        db.Integer, nullable=False,
        primary_key=True, auto_increment=True
    )
    insert_date = db.Column(
        db.DateTime, default=datetime.datetime.utcnow,
        nullable=False
    )
    update_date = db.Column(
        db.DateTime, default=datetime.datetime.utcnow,
        nullable=False, onupdate=datetime.datetime.utcnow
    )
