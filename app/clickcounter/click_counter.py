#!/usr/bin/env python2

import datetime
import time

import psycopg2

from flask import Flask, request, render_template

app = Flask(__name__)

conn = None
while not conn:
    try:
        conn = psycopg2.connect(host="db", dbname="click_counter", user="docker", password="dbpass")
    except Exception:
        print "Failed to connect to db, retrying"
        time.sleep(1)

cur = conn.cursor()


@app.route('/')
def hello_world():
    add_hit(request.remote_addr, datetime.datetime.now())
    return render_template("index.html", hits=get_hits(), count=get_count())

def get_count():
    cur.execute("SELECT count(*) FROM hits;")
    result = cur.fetchone()
    return result[0]

def get_hits():
    cur.execute("SELECT * FROM hits;")
    return cur.fetchall()


def add_hit(ip, tm):
    cur.execute("INSERT INTO hits (ip, time) VALUES (%s, %s)", (ip, tm))
    conn.commit()

def init_db():
    cur.execute("CREATE TABLE IF NOT EXISTS hits (id serial PRIMARY KEY, ip varchar, time timestamp);")
    conn.commit()


if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0")
