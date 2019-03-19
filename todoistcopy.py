import sqlite3
import datetime
import random

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
        self.cur.execute("INSERT INTO task (userid, name, descr, timeset, dateterm, timeterm) VALUES (?,?,?,?,?,?)",
                         (self.id, taskobj.name, taskobj.descr, taskobj.timeset, taskobj.dateterm, taskobj.timeterm))
        taskobj.id = self.cur.execute("SELECT id FROM task WHERE rowid=last_insert_rowid()").fetchone()[0]
        taskobj.userid = self.id
        self.connectclose()

    def addproject(self, projectobj):
        self.connect()
        self.cur.execute("INSERT INTO project (userid, name, descr, timeset) VALUES (?,?,?,?)",
                         (self.id, projectobj.name, projectobj.descr, projectobj.timeset))
        projectobj.id = self.cur.execute("SELECT id FROM project WHERE rowid=last_insert_rowid()").fetchone()[0]
        projectobj.userid = self.id
        self.connectclose()


class task(dbase):

    id = 0
    userid = 0
    parentid = 0
    projectid = 0
    name = ''
    descr = ''
    timeset = datetime.datetime.now()
    dateterm = ''
    timeterm = ''

    def __init__(self, name, descr="NULL", dateterm="NULL", timeterm="NULL", parentid=0, projectid=0):
        self.parentid = parentid
        self.projectid = projectid
        self.name = name
        self.descr = descr
        self.dateterm = dateterm
        self.timeterm = timeterm

class project(dbase):

    id = 0
    userid = 0
    name = ''
    descr = ''
    timeset = datetime.datetime.now()

    def __init__(self, name, descr="NULL"):

        self.name = name
        self.descr = descr


usr = user('vasya', 'vasya')
tsk = task("novay" + str(random.randint(0,10000)), "opis")
prj = project('novyi' + str(random.randint(0,10000)), 'opisanie proekta')
usr.addtask(tsk)
usr.addproject(prj)
