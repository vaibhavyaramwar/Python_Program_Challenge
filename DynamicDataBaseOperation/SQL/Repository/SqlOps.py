import mysql.connector as connection

def createtable(hostname,portno,username,password,database,query):
    try:

        myDb = connection.connect(host=hostname, port=portno, user=username, password=password, database=database,use_pure=True)
        cursor = myDb.cursor()
        cursor.execute(query)
        myDb.close()

    except Exception as e:
        myDb.close()
        print(e)

def getDatabases(hostname,portno,username,password):
    try:

        myDb = connection.connect(host=hostname, port=portno, user=username, password=password,use_pure=True)
        cursor = myDb.cursor()
        databases = cursor.execute("show databases")
        myDb.close()

        return databases
    except Exception as e:
        myDb.close()
        print(e)

def getTables(hostname,portno,username,password):
    try:

        myDb = connection.connect(host=hostname, port=portno, user=username, password=password,use_pure=True)
        cursor = myDb.cursor()
        tables = cursor.execute("show tables")
        myDb.close()

        return tables
    except Exception as e:
        myDb.close()
        print(e)