import pypyodbc

def connectToDatabase(driver, ip, port, db_name, user_ID, password):
    connect_str = ('DRIVER={'+driver+'};'
                + 'SERVER=' + ip + ',' + port + ';'
                  + 'UID=' + user_ID + ';'
                  + 'PWD=' + password + ';')
    print(connect_str)
    try:
        conn = pypyodbc.connect(connect_str)
        cursor = conn.cursor()
        #cursor.execute("SELECT * from dpFund")
        row = cursor.execute("SELECT top 100 * from dpFund").fetchone()
        #cursor.commit()
        print(row)
        return conn
    except Exception as e:
        print(e)
    
    #return pypyodbc.connect(connect_str)
    #print(connect_str)

def sqlWithResults(conn, sql_str):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * from dpFund")
        cursor.commit()
        print(cursor.fetchall())
    except Exception as e:
        print('Execution error.')
        print(e)

if __name__ == "__main__":
    conn = connectToDatabase('SQL Server', '112.74.196.62', '1433', 'jydb_all', 'dpadmin', 'dpadmin')
    #if conn:
     #   sql_str = 'select * from dbo.dpDict'
      #  sqlWithResults(conn, sql_str)
