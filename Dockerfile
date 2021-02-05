FROM python:3.7-alpine
MAINTAINER Jay Dhanani

# Runs python in unbuffered environment
ENV PYTHONUNBUFFERED 1

# For installing the requirements
COPY ./requirements.txt /requirements.txt

# Here we required some packages to install our python requirements however we don't required to execute it further
# so we install it temporarily and give it name .tmp-build-deps and after installing python requirements we delete those packages
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers musl-dev
# To install mysql on server
RUN apk add --update --no-cache mariadb-dev

# Installing the requirements
RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps


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
