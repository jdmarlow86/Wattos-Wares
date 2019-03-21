import sqlite3
from sqlite3 import Error

def main():
    database = '/Users/J&E/Desktop/MissionU/Wattos_Wares.db'
 
    # create a database connection
    conn = sqlite3.connect(database)
    with conn:
        print("1. Query all planets")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Planets")
 
        rows = cur.fetchall()
 
        for row in rows:
            print(row)

        print("\n")
        print("2. Now query Outer Rim planets")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Planets WHERE Planets.Sector='Outer Rim'")
 
        rows = cur.fetchall()
 
        for row in rows:
            print(row)
    
 
if __name__ == '__main__':
    main()
