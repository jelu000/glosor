import sqlite3

class glosor:

    def __init__(self):
        self.dbname="glosor.db"
        self.table_name = 'glostable'
        self.create_table()

    def my_drop_table(self):

        conn = sqlite3.connect(self.dbname)
        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()
        print("drop TAble")
        
        # Execute the DROP TABLE statement
        print(f"dbname = {self.table_name}")
        input("Mata In")
        cursor.execute(f'''DROP TABLE glostable''')

        # Commit the transaction to make the change permanent
        conn.commit()

        # Close the database connection
        conn.close()

    #----------------------------------------------------------------------------------------------------    
    #Skapar tabellen i databasen, körs bara första gången
    def create_table(self):
        try:
            sqliteConnection = sqlite3.connect(self.dbname)
            sqlite_create_table_query = f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                                id INTEGER PRIMARY KEY,
                                swglosa TEXT NOT NULL,
                                englos TEXT NOT NULL);'''

            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")

            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")
        


    def add_glosa_to_table(self, sv_glosa, en_glosa):
        try:
            sqliteConnection = sqlite3.connect(self.dbname)
            sqlite_create_table_query = f'''INSERT INTO {self.table_name} (
                                {sv_glosa},
                                {en_glosa})'''

            cursor = sqliteConnection.cursor()
            #print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")
