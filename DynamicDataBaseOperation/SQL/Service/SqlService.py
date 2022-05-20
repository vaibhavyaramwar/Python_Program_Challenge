from SQL.Repository import SqlOps

def createtable(hostname,portno,username,password,database,tablename,tableColumns):

    createTableQuery = "create table if not exists "+hostname+"."+tablename+"("
    try:

        print(SqlOps.getDatabases(hostname,portno,username,password))
        print(SqlOps.getTables(hostname,portno,username,password))


        if type(tableColumns) == dict:
            for col,dtype in tableColumns.items():
                createTableQuery = createTableQuery+col+" "+dtype+","
            createTableQuery = createTableQuery[0:len(createTableQuery)-1]
            createTableQuery = createTableQuery+")"
            SqlOps.createtable(hostname,portno,username,password,database,createTableQuery)

        else:
            pass
    except Exception as e:
        pass