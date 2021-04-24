FROM python:3.8

RUN pip install rq

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD reddit_collector ./reddit_collector

CMD ["rq", "worker"]
