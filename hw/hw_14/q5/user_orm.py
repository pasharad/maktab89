from peewee import SqliteDatabase, Model, CharField, DateField
from pydantic import BaseModel

db = SqliteDatabase("users.db")

class Users(Model):
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)
    creation_date = DateField()

    class Meta:
        database = db

try:
    with db:
        db.create_tables([Users])

except Exception as e: 
    print(f"Failed to create table!{e}")

