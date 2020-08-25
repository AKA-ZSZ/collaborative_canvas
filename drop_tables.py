from database import db
from database import User, Pixels

def drop():
    db.drop_tables([User])
    db.drop_tables([Pixels])
