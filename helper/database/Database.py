import mysql.connector
from helper.singleton.singleton import singleton



@singleton
class Database():
    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="shitduck.duckdns.org",
                    user="root",
                    password="admin12345",
                    database="PythonDatabase"
        )
        self.cursor = self.mydb.cursor()


    def __del__(self):
        self.cursor.close()
        self.mydb.close()

    def set_database(self,database):
        self.mydb = database
    def get_database(self):
        return self.mydb
    def del_database(self):
        self.mydb.close()
        del self.mydb

    def set_cursor(self,cursor):
        self.usecursorrname = cursor
    def get_cursor(self):
        return self.cursor
    def del_cursor(self):
        self.cursor.close()
        del self.cursor
