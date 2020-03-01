from flask import Flask
from flask import abort,jsonify
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
import settings
import ast

def make_celery(app):
    celery = Celery(
        'clelery_instance',
        backend=settings.CELERY_RESULT_BACKEND,
        broker=settings.CELERY_BROKER_URL
    )
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

app = Flask(__name__)

celery = make_celery(app)

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=settings.DATABASE.get('USER'),pw=settings.DATABASE.get('PASSWORD'),url=settings.DATABASE.get('HOST')+':'+settings.DATABASE.get('PORT'),db=settings.DATABASE.get('NAME'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)

class api_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), unique=False)


@celery.task()
def getData():
    response = api_data.query.all()
    response_array = []
    for i in (response):
        response_array.append(i.text)
    f = open("trainResultData/trainDump", "w")
    f.write(str(response_array))
    f.close()
    return('train done')

@app.errorhandler(404)
def page_not_found(e):
    error=str(e)
    return jsonify({"message":404, "description":error}),404

@app.route('/')
def home():
    return jsonify({"message": 200, "description": 'wellcome'})

@app.route('/train')
def train():
    result = getData.delay()
    return jsonify({"message": 202, "description": 'training started...'}),202

@app.route('/predict')
def predict():
    try:
        f = open("trainResultData/trainDump", "r")
        f_array = ast.literal_eval(f.read())
    except IOError:
        return abort(404, description="train result not found!")
    return jsonify({"message": 200, "result": f_array})

@app.route('/ping', methods=['GET'])
def ping(): 
  return jsonify({"message": 200, "description": 'PONG'})
