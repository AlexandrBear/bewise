from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from models import *
from config import Configuration
import requests


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)


def save_data(response):
    count = 0
    for i in response:
        card = db.session.query(Card).filter(Card.id == f'{id}').all()
        if not card:
            data = Card(id=i['id'], answer=i['answer'], question=i['answer'])
            db.session.add(data)
            db.session.commit()
        else:
            count += 1
    if count != 0:
        get_questions(count)
    else:
         print('OK')
    


def get_questions(number: int):
    url = 'https://jservice.io/api/random?count={}'.format(number)
    response = (requests.get(url)).json()
    save_data(response)

    if response != []:
        return(response[-1]['question'])
    else:
        return []


@app.route("/", methods=['post', 'get'])
def index():
    message = ''
    if request.method == 'POST':
        number = request.form.get('num')
        if number.isnumeric():
            message = get_questions(number)
        else:
            message = 'Вы ввели не число.'
        
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0')