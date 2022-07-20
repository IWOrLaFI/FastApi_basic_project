#
# import sqlalchemy
# from .database import metadata
# import datetime
#
# users = sqlalchemy.Table(
#     "users",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
#     sqlalchemy.Column("username", sqlalchemy.String, primary_key=True, unique=True),
#     sqlalchemy.Column("first_name", sqlalchemy.String),
#     sqlalchemy.Column("last_name", sqlalchemy.String),
#     sqlalchemy.Column("phone_number", sqlalchemy.String, primary_key=True, unique=True),
#     sqlalchemy.Column("birthday", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
#     sqlalchemy.Column("updated_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
#     sqlalchemy.Column("hashed_password", sqlalchemy.String)
# )