import sqlite3

class Player(object):
    def __init__(self, tablename="Players", Id="Id", password="password", username="username", NumOfWins = "Number_of_wins"):
        self.__tablename = tablename
        self.__Id = Id
        self.__password = password
        self.__username = username
        self.__NumOfWins = NumOfWins

        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__Id + " " + "INTEGER PRIMARY KEY AUTOINCREMENT,"
        str += " " + self.__password + " TEXT    NOT NULL,"
        str += " " + self.__username + " TEXT    NOT NULL,"
        str += " " + self.__NumOfWins + " NUM)"
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def insert_player(self, username, password):
        try:
            conn = sqlite3.connect('test.db')
            str_insert = "INSERT INTO " + self.__tablename + " (" + self.__password + ", " + self.__username + ", " + self.__NumOfWins + ") VALUES (" + "'" + password + "'" + ", " + "'" + username + "', '" + str(0) + "')"
            print(str_insert)
            conn.execute(str_insert)
            print("worked")
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert player")
            return False

    def return_player_by_username_and_password(self, username, password):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        strsql = "SELECT * from " + self.__tablename + " where " + self.__username + " = '" + str(username) + "' & " + self.__password + " = '" + str(password) + "'"
        print(strsql)
        cursor = conn.execute(strsql)
        row = cursor.fetchone()
        if row:
            print("player exists")
            c = print("success")
            conn.commit()
            conn.close()
            return [row[1], row[2], row[3] + c]


        else:
            print("Failed to find player")
            conn.commit()
            conn.close()
            return False








p = Player()
p.insert_player("user", "pass")
p.return_player_by_username_and_password("user", "pass")