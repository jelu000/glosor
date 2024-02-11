import sqlite3

class glosor:

    def __init__(self):
        self.dbname="glosor.db"
        self.table_name = 'glostable'
        

    def my_delete_table(self):

        conn = sqlite3.connect(self.dbname)
        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()
        #print("drop TAble")
        
        # Execute the DELETE TABLE statement
        #print(f"dbname = {self.table_name}")
        #input("Mata In")
        deletetable = f"DELETE FROM {self.table_name}"
        cursor.execute(deletetable)

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
            #print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            #print("SQLite table created")

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
                          ('{sv_glosa}', '{en_glosa}') """

            
            
            
            cursor = sqliteConnection.cursor()
            cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()#OBS GLÖM EJ DENNA RAD
            cursor.close()
            print(f"\n\tSuccessfully added glosa {sv_glosa} och {en_glosa}")


        except sqlite3.Error as error:
            print("add_glosa: Error while creating a sqlite table", error)
        
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                #print("sqlite connection is closed")


    def get_glosor_from_db(self):
        
        glos_dict = {}

        try:
            #Skapar DB connection och databas fråga som sen körs/executes
            sqliteConnection = sqlite3.connect(self.dbname)
            cursor = sqliteConnection.cursor()
            #print("Connected to SQLite")
            sqlite_select_query = f"SELECT * from {self.table_name}"
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            #Lägger till varje hund i databasen till hundlistan  
            for row in records:
                glos_dict.update({row[1] : row[2]})
                
            #stänger cursor objektet     
            cursor.close()
        #skriver ut fel om det uppstår
        except sqlite3.Error as error:
            print("get_glosor-Failed to read data from sqlite table", error)
        #stänger databas koppling 
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

        return glos_dict