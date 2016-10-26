FROM debian:latest

RUN apt-get update
RUN apt-get install -q -y python python-dev python-pip libpq-dev vim net-tools

COPY ./clickcounter/requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY ./clickcounter /clickcounter
WORKDIR /clickcounter

EXPOSE 5000

#CMD ["/usr/bin/gunicorn", "-b 0.0.0.0:5000", "--error-logfile -", "list_server:app"]
CMD ["python", "click_counter.py"]
