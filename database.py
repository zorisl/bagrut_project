import sqlite3

class Players(object):
    def __init__(self, tablename = "Players", ID = "Id", email = "email", password = "password", name = "name", NumOfWins = "Number of wins"):
        self.__tablename = tablename
        self.__ID = ID
        self.__email = email
        self.__password = password
        self.__name = name
        self.__NumOfWins = NumOfWins

        conn = sqlite3.connect('test1.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.ID + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__email + " TEXT    NOT NULL ,"
        str += " " + self.__password + " TEXT    NOT NULL, "
        str += " " + self.__NumOfWins + " NUM) "
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def get_email(self, email):


    def check_email(self, email):
        if(get_email == true)
            return false
        else return true

    def insert_user(self, name, email, password):
        conn = sqlite3.connect('test1.db')
        while(check_email == true)
