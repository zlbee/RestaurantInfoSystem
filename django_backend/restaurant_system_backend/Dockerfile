# use official python:3.12 as base image
FROM python:3.12

# setup environment
ENV PYTHONUNBUFFERED=1
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432

# setup working directory
WORKDIR /code/django_backend

# copy the dependency file
COPY requirements.txt /code/django_backend/

# install project dependency
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project file to the working directory
COPY . /code/django_backend/