import Data.assignData
from Data.dataClasses import *

#Class to hold the patient master list and the currently logged in user
class System():
    TheSystem = None #Class variable to hold itself in so that other classes can make calls to the System class and access it
    def __init__(self):
        System.TheSystem = self #Store self into class variable upon creation
        
        self.patientList = []
        self.user = User()
        patientCreator = Data.assignData.patientList()
        patientCreator.createList()
        self.patientList = patientCreator.getList()

#create a system object to initialize TheSystem variable above
def initialize():
    system = System()

#Returns current master list of patients
def getPatientList():
    return System.TheSystem.patientList

def getUser():
    return System.TheSystem.user