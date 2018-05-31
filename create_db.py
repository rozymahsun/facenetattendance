import sqlite3
conn = sqlite3.connect('attendance.db')
c = conn.cursor()
sql1 = """
DROP TABLE IF EXISTS users;
CREATE TABLE users (
           user_id integer unique primary key autoincrement,
           name text
);
"""
sql2 = """
DROP TABLE IF EXISTS attendance;
CREATE TABLE attendance (
           att_id integer unique primary key autoincrement,
           name text,
           cekinout integer(4) not null default (strftime('%s','now'))
);
"""

c.executescript(sql1);
c.executescript(sql2);

conn.commit()
conn.close()