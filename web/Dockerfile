# Dockerfile

# Pull base image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /proj

ADD ./requirements.txt /proj/requirements.txt

RUN pip install -r requirements.txt

ADD . /proj

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

