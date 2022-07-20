from ..db.database import metadata, engine, Base
from ..db.users import users

Base.metadata.create_all(bind=engine)
