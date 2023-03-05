import mysql.connector

class myConnector():
    def __init__(self):

        self.connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="PIMS2023"
        )

        self.myCursor = self.connection.cursor()

    #takes mySQL command(string) and executes
    def execute(self, cmnd):
        self.myCursor.execute(cmnd)

    #fetches all database data from executed statement
    def fetch(self):
        return self.myCursor.fetchall()
    
    #add column to database
    def addColumn(self, colName):
        query = "ALTER TABLE patient_info ADD " + colName + " text;"
        self.myCursor.execute(query)
        self.connection.commit()

    #update database by column
    def update(self, col, data, id):
        #column name, data being updated, patient id
        query = "UPDATE patient_info\n SET " + col + " = " + data + "\nWHERE patient_ID = " + id
        self.myCursor.execute(query)
        self.connection.commit()

    def checkRowCount(self):
        rows = self.execute("SELECT * FROM patient_info")
        return rows