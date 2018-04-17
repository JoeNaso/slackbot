FROM python:3
MAINTAINER Joe Naso <

COPY ./requirements.txt config/pip.txt
RUN pip install --upgrade pip && \
    pip install -r config/pip.txt

# Copy working dir
COPY ./app/ /home/docker/slackbot/

WORKDIR /home/docker/slackbot/

EXPOSE 5000