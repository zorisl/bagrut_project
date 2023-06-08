import sqlite3

class User(object):
    def __init__(self, tablename = "Users", Id = "Id", username = "username", password = "password", NumOfWins = "NumOfWins"):
        self.__tablename = tablename
        self.__Id = Id
        self.__username = username
        self.__password = password
        self.__NumOfWins = NumOfWins

        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")
        str = "CREATE TABLE IF NOT EXISTS " + self.__tablename + "(" + self.__Id + " " + "INTEGER PRIMARY KEY AUTOINCREMENT ,"
        str += " " + self.__username + " TEXT    NOT NULL ,"
        str += " " + self.__password + " TEXT    NOT NULL, "
        str += " " + self.__NumOfWins + " NUM)"
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()
    def get_table_name(self):
        return self.__tablename
    def select_all_users(self):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully");
            str1 = "select*from " + self.__tablename
            print(str1)
            cursor = conn.execute(str1)
            rows = cursor.fetchall()
            arr_users = []
            for row in rows:
                str_rows = str(row[0]) + " " + row[1] + " " + str(row[2])
                arr_users.append(str_rows)
            print(arr_users)
            return arr_users
        except:
            return False
    def insert_user(self, username, password):
        try:
            conn = sqlite3.connect('test.db')
            str_insert = "INSERT INTO " + self.__tablename + " (" + self.__username + "," + self.__password + ") VALUES (" + "'" + username + "'" + "," + "'" + password + "');"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert user")
            return False
    def delete_by_username(self, username):
        try:
            conn = sqlite3.connect('test.db')
            str_delete = "DELETE  from " + self.__tablename + " where " + self.__username + "=" + "'" + username +"'"
            print(str_delete)
            conn.execute(str_delete)
            conn.commit()
            conn.close()
            print("Record deleted successfully")
            return "Success"
        except:
            return "Failed to delete user"
    def return_user_by_username(self, username):
        try:
            conn = sqlite3.connect('test.db')
            print("Opened database successfully")
            strsql = "SELECT * from " + self.__tablename + " where " + self.__username + "=" + "'" + username + "'"
            print(strsql)
            cursor = conn.execute(strsql)
            row = cursor.fetchone()
            if row:
                return [row[0], row[1], row[2]]
            else:
                print("Failed to find user")
                return False
            conn.commit()
            conn.close()
        except:
            return False
    def __str__(self):
        return "table  name is ", self.__tablename


u = User()