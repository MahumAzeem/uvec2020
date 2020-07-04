import sqlite3

sqlite_file = "kira.db"

def run():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS tasks 
        (title string NOT NULL,
        description string
        )''')

    #commit the changes to db			
    conn.commit()
    #close the connection
    conn.close()