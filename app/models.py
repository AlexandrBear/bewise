from app import db
from sqlalchemy import Column
import time
from datetime import datetime
from sqlalchemy import create_engine
from config import Configuration


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text)
    question = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Card, self).__init__(*args, **kwargs)
        self.id = self.id

        
    def __repr__(self) -> str:
        return '<Card id: {}, question: {}>'.format(self.id, self.question)

engine = create_engine(Configuration.SQLALCHEMY_DATABASE_URI)

while True:
    try:
        engine.connect()
        print('YYES')
        db.create_all()
        break
    except:
        print('Ждем подлючение к базе')
        time.sleep(2)