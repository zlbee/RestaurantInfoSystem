# use official python:3.12 as base image
FROM python:3.12

# setup env
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres

# setup working directory
WORKDIR /code/flask_backend

# copy the dependency file
COPY requirements.txt /code/flask_backend/

# install project dependency
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project file to the working directory
COPY . /code/flask_backend/