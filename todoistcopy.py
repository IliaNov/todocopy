import sqlite3
import datetime

class dbase:
    conn = None
    cur = None

    def connect(self):
        self.conn = sqlite3.connect("todoistcopydb.db")
        self.cur = self.conn.cursor()

    def connectclose(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


class user(dbase):
    id = 0

    def __init__(self, login, password):
        if not self.authorise(login, password):
            return None

    def authorise(self, login, password):
        self.connect()
        self.cur.execute("SELECT id FROM user WHERE name=? and password=?", (login, password))
        id = self.cur.fetchone()[0]
        if id != 0:
            self.id = id
            self.connectclose()
            return True
        else:
            self.connectclose()
            return False

    def addtask(self, taskobj):
        self.connect()
        self.cur.execute("INSERT INTO usertask (userid, taskid) VALUES (?,?)", (self.id, taskobj.id))
        self.connectclose()


class task(dbase):

    id = 0

    def __init__(self, name, descr="NULL", dateterm="NULL", timeterm="NULL"):
        self.connect()
        self.cur.execute("INSERT INTO task (name, descr, timeset, dateterm, timeterm) VALUES (?,?,?,?,?)",
                         (name, descr, datetime.datetime.now(), dateterm, timeterm))
        self.id = self.cur.execute("SELECT id FROM task WHERE rowid=last_insert_rowid()").fetchone()[0]
        self.connectclose()


class project(dbase):

    id = 0

    def __init__(self, name, descr="NULL"):

        self.connect()
        self.cur.execute("INSERT INTO project (name, descr, timeset) VALUES (?,?,?)",
                         (name, descr, datetime.datetime.now()))
        self.id = self.cur.execute("SELECT id FROM project WHERE rowid=last_insert_rowid()").fetchone()[0]
        self.connectclose()



usr = user('vasya', 'vasya')
tsk = task("novay", "opis")
prj = project('novyi', 'opisanie proekta')
usr.addtask(tsk)
