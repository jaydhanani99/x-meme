FROM python:3.7-alpine
MAINTAINER Jay Dhanani

# Runs python in unbuffered environment
ENV PYTHONUNBUFFERED 1

# For installing the requirements
COPY ./requirements.txt /requirements.txt

# Installing the requirements
RUN pip install -r /requirements.txt

# Creating application directory in docker image
RUN mkdir /app
# Setting default working directory as app
WORKDIR /app
# Copying our app directory to docker app directory
COPY ./app /app

# Adding user to docker container
RUN adduser -D user
# Switching to user
USER user
