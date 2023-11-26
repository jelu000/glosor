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
        #print("drop TAble")
        
        # Execute the DROP TABLE statement
        print(f"dbname = {self.table_name}")
        #input("Mata In")
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
                                englosa TEXT NOT NULL);'''

            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")

            cursor.close()

        except sqlite3.Error as error:
            print("create_table_Error while creating a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")
        
    #------------------------------------------------------------------------------------------------------------
    #Lägg till glosa till db

    def add_glosa_to_table(self, sv_glosa, en_glosa):
        try:
            sqliteConnection = sqlite3.connect(self.dbname)
            
            sqlite_insert_query = f"""INSERT INTO {self.table_name}
                          (swglosa, englosa)  
                          VALUES  
                          ('{sv_glosa.capitalize()}', '{en_glosa.capitalize()}') """

            cursor = sqliteConnection.cursor()
            cursor.execute(sqlite_insert_query)
            cursor.close()
            #print("Successfully added glosa and Connected to SQLite")


        except sqlite3.Error as error:
            print("add_glosa: Error while creating a sqlite table", error)
        
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                #print("sqlite connection is closed")
