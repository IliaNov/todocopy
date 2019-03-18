import sqlite3



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
            return None;


    def authorise(self, login, password):
        self.connect()
        self.cur.execute("SELECT id FROM user WHERE name=? and password=?", (login, password))
        id = self.cur.fetchone()[0]
        if id !=0:
            self.id = id
            self.connectclose()
            return True
        else:
            self.connectclose()
            return False

    def addtask(self, task):
        self.connect()
        self.cur.execute("INSERT INTO usertask (userid, taskid) VALUES (?,?)", (self.id, task.id))
        self.connectclose()





class task(dbase):
    id = 0
    def __init__(self, name, descr = "NULL", dateterm = "NULL", timeterm = "NULL"):
        self.connect()
        self.cur.execute("INSERT INTO task (name, descr, dateterm, timeterm) VALUES (?,?,?,?)",(name, descr, dateterm, timeterm))
        self.id = self.cur.execute("SELECT id FROM task WHERE rowid=last_insert_rowid()").fetchone()[0]
        self.connectclose()


class project(dbase):
    def __init__(self):
        print('project')


usr = user('vasya', 'vasya')
#tsk = task("novay", "opis")
#usr.addtask(tsk)
