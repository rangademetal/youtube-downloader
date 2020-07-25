import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connection(self):
        con = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        return con

    def getQuery(self, con, sql):
        arr = []
        con = con.cursor()
        con.execute(sql)
        rs = con.fetchall()
        for x in rs:
            arr.append(x)
        return arr