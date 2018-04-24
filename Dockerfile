FROM python:3
MAINTAINER Joe Naso

COPY ./docker-config/requirements.txt config/pip.txt
RUN pip3 install --upgrade pip && \
    pip3 install -r config/pip.txt

# Copy working dir
COPY ./web/ /home/docker/slackbot/

WORKDIR /home/docker/slackbot/

EXPOSE 5000
CMD []