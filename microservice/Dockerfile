FROM python:3

WORKDIR /srv

ADD ./requirements.txt /srv/requirements.txt

RUN pip install -r requirements.txt

ADD . /srv

RUN export FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
