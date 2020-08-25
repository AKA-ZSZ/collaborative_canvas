from database import db
from database import User, Pixels

def create():
    db.create_tables([User])
    db.create_tables([Pixels])
