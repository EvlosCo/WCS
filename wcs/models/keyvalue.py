from wcs.models import BaseModel, db


class KeysValues(BaseModel):
    key = db.Column(db.String(80), nullable=False, unique=True)
    value = db.Column(db.UnicodeText, nullable=False)
