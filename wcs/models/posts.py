from wcs.models import BaseModel, db


class Posts(BaseModel):
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('Users.id'))
    user = db.relationship('Users', back_populates='posts')
    title = db.Column(db.String(80), nullable=False, default='Untitled')
    content = db.Column(db.UnicodeText, nullable=False)
