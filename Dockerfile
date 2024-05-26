# start from an official image
FROM python:3.10.0
ARG APP_VERSION=0.0.1
ARG DEBIAN_FRONTEND=noninteractive

# set workdir
WORKDIR /app

# copy project
COPY . /app

# install dependencies
RUN pip install -r requirements.txt

# expose port \
EXPOSE 8000