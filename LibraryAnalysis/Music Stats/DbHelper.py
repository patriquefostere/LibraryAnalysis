import pyodbc

def DoFetch(query):
    connection = Connect()#todo: move this?
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except:
        print("bad query in DoFetch: ", query)
    return cursor.fetchall()


def DoInsertOrUpdate(query):
    connection = Connect()#todo: move this?
    cursor = connection.cursor()

    try:
        cursor.execute(query)
    except:
        print("bad query in DoInsertOrUpdate: ", query)
    
    connection.commit()


def Connect():
    SERVER = r'VIVIAN\SQLEXPRESS'
    DATABASE = 'MusicManagement'

    connectionString = f'DRIVER={{SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};Trusted_connection=yes'

    return pyodbc.connect(connectionString)

