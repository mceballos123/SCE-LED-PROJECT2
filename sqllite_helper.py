import sqlite3
from tabulate import tabulate
from fastapi import HTTPException
def create_table(db_file):
    con=sqlite3.connect(db_file)

    cursor_obj=con.cursor()
    #cursor_obj.execute("DROP TABLE IF EXISTS")

    query_table="""CREATE TABLE IF NOT EXISTS users(
    
            username TEXT PRIMARY KEY,
            total_solved INTEGER,
            points INTEGER,
            easy_solved INTEGER DEFAULT 0,
            medium_solved INTEGER DEFAULT 0,
            hard_solved INTEGER DEFAULT 0
    
    );

        """
    
    cursor_obj.execute(query_table)

    print("Table is ready")
    con.close()

def add_user(db_file,username,total_solved,points,easy_solved,medium_solved,hard_solved):
        con=sqlite3.connect(db_file)
        cursor_obj=con.cursor()
        
        #cursor_obj.execute(query_table)
        query_table="INSERT INTO users(username,total_solved,points,easy_solved,medium_solved,hard_solved)   VALUES(?,?,?,?,?,?)"
        cursor_obj.execute(query_table,(username,total_solved,points,easy_solved,medium_solved,hard_solved))
                      
        print("Inserting Data...")

        data=cursor_obj.execute('''SELECT * FROM users''')

        for row in data:
            print(row)
        
        con.commit()
        con.close()

def update_user(db_file,username,total_solved,points,easy_solved,medium_solved,hard_solved):
    conn=sqlite3.connect(db_file)
    cursor=conn.cursor()
    query_table="UPDATE users SET total_solved=?, points=?,easy_solved=?,medium_solved=?,hard_solved=? WHERE username=?"
    #(username,total_solved,points,easy_solved,medium_solved,hard_solved)
    #execute_command(constants.update_user_query_table)
   
    data=cursor.execute(query_table,(username,total_solved,points,easy_solved,medium_solved,hard_solved))
    
    for row in data:
        print(row)
    
    conn.commit()
    conn.close()
    
def display_all_user(db_file):
    #Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Execute query to get all users
    cursor.execute('SELECT * FROM users')
    output = cursor.fetchall()

    # Extract column names for headers
    column_names = [description[0] for description in cursor.description]

 

    # Display the table
    if output:
        print("Displaying all registered users")
        print(tabulate(output, headers=column_names, tablefmt="grid"))
    else:
        print("No users found in the database.")
    
    

    # Close connection
    conn.close()
    return output


def top_user(db_file):
    conn=sqlite3.connect(db_file)
    cursor=conn.cursor()
    print(f"Connect to db")

    query_table="SELECT * FROM users ORDER BY points DESC LIMIT 3 "
    cursor.execute(query_table)
    print(f"Query Executed")
    data=cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    
    if data:
        print("Showing the top 3 leetcode users")
        print(tabulate(data, headers=column_names, tablefmt="grid"))
    else:
        print("No users found in the database.")

    conn.commit()
    conn.close()
    return data
    #use desc


def check_user_exists(db_file,username):
    conn=sqlite3.connect(db_file)
    curr=conn.cursor()
    query_table="SELECT COUNT(1) FROM users WHERE username=? LIMIT 1  "

    curr.execute(query_table,(username,))
    exisiting_user=curr.fetchone()

    conn.commit()
    conn.close()
    
    if(exisiting_user):
        #raise HTTPException(detail="User already registered")
        return False
    
    else:
        print("User given is not registered")
        return True
    
    
    
    

def get_first_place(db_file):
    conn=sqlite3.connect(db_file)
    curr=conn.cursor()
    query_table="SELECT * FROM users ORDER BY points DESC LIMIT 1 "

    curr.execute(query_table)
    column_names = [description[0] for description in curr.description]

    data=curr.fetchall()
    print("Showing the top user")

    #print(data)
    if(data):
        print(tabulate(data, headers=column_names, tablefmt="grid"))

    else:
        print("No users added")
    
    conn.commit()
    conn.close()
    return data



def delete_user(db_file,username):
    conn=sqlite3.connect(db_file)
    curr=conn.cursor()

    query_table='DELETE FROM users WHERE username=?'
    curr.execute(query_table,(username,))

    conn.commit()
    conn.close()

