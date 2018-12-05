from wcs.models import BaseModel, db


class RolesUsersAssociation(BaseModel):
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('Users.id'))
    role_id = db.Column('role_id', db.Integer, db.ForeignKey('Roles.id'))


class Roles(BaseModel):
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    users = db.relationship('Users', back_populates='roles')


class Users(BaseModel):
    username = db.Column(
        db.String(80), nullable=False, unique=True
    )
    email = db.Column(
        db.String(80), nullable=False, unique=True
    )
    _password = db.Column(
        db.String(80), nullable=False
    )
    avatar_url = db.Column(
        db.Text, nullable=False
    )
    posts = db.relationship('Posts', back_populates='user')
    roles = db.relationship('Roles', back_populates='users')
