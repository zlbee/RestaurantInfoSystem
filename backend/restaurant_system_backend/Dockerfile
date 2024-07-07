# use official python:3.12 as base image
FROM python:3.12

ENV PYTHONUNBUFFERED=1

# setup working directory
WORKDIR /code

# copy the dependency file
COPY requirements.txt /code/

# install project dependency
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project file to the working directory
COPY . /code/