from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField
from flask_login import UserMixin

db = SqliteDatabase('pixr.sqlite')
db.connect()


class User(UserMixin, Model):
    """ Peewee model for Abstract Unit """
    username = CharField(unique=True)
    password = CharField()

    def __str__(self): return self.username

    class Meta:
        database = db


class Pixels(Model):
    """ Peewee model for the canvas """
    user = ForeignKeyField(User)
    pixel = CharField()
    color = CharField()

    class Meta:
        database = db

    def __str__(self): return self.user


if __name__ == "__main__":
    db.drop_tables([User, Pixels])
    db.create_tables([User, Pixels])
    user = User.create(username='test', password='password')
    home = User.create(username='home', password='none')

