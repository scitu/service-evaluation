FROM python:3.6

RUN apt-get update &&\
    apt-get install -y unixodbc unixodbc-dev postgresql postgresql-contrib\
        graphviz libgraphviz-dev pkg-config
RUN mkdir /web
WORKDIR /web
ADD ./requirements.txt /web/requirements.txt
RUN pip install -r requirements.txt
COPY . /web/
