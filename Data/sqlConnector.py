import mysql.connector

class myConnector():
    def __init__(self):

        self.connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="PIMS2023"
        )

        self.myCursor = self.connection.cursor()
        self.myCursor.execute("use patient_information;")

    # execute SQL commands
    def execute(self, cmd):
        self.myCursor.execute(cmd)

    # returns all data given a statement
    def fetch(self):
        return self.myCursor.fetchall()
    
    # add column to database
    def addColumn(self, colName):
        query = "ALTER TABLE patients ADD " + colName + " text;"
        self.myCursor.execute(query)
        self.connection.commit()

    # update database by column
    def update(self, col, data, id):
        #column name, data being updated, patient id
        query = "UPDATE patients\n SET " + col + " = " + data + "\nWHERE patient_ID = " + id
        self.myCursor.execute(query)
        self.connection.commit()

    # returns amount of rows in table
    def checkRowCount(self):
        query = "SELECT COUNT(*) FROM patients"
        self.myCursor.execute(query)
        rows = self.fetch()
        rows = int(rows[0][0])
        return rows