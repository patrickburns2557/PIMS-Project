import Data.assignData
import GUI.MainWindow
from Data.dataClasses import *


# Class to hold the patient master list and the currently logged-in user
class System:
    TheSystem = None  # Class variable to hold itself in so that other classes can make calls to the System class and access it

    def __init__(self):
        System.TheSystem = self  # Store self into class variable upon creation

        self.patientList = []
        self.user = User()

    def loadPlaceholderData(self):
        p1 = Patient()
        p1.setFirstName("Barry")
        p1.setMiddleName("Andrew")
        p1.setLastname("Matthews")
        p1.setAddress(["918 Main Road", "Huntsville", "Alabama", "35776"])
        p1.setHomePhone("555-123-4567")
        p1.setWorkPhone("555-456-7890")
        p1.setMobilePhone("555-789-0234")
        p1.addEmergencyContact("Emergency contact name 1", "555-233-4566")
        p1.addEmergencyContact("Emergency contact name two", "555-455-6788")
        p1.addEmergencyContact("Emergency contact name 3", "555-455-6788")
        p1.setNumAllowedVisitors("3")
        p1.addAllowedVisitor("Visitor 1")
        p1.addAllowedVisitor("Bob Jones")
        p1.addAllowedVisitor("George Washington")
        p1.addAllowedVisitor("Visitor 4")
        p1.setLocation(["Facility 7", "Floor 2", "Room 213", "Bed 1"])
        p1.setFamilyDoctor("Dr. Medical Doctor Man")
        p1.setDateAdmittance("January 17, 2020")
        p1.setTimeAdmittance("7:15PM")
        p1.setDateDischarge("April 2, 2020")
        p1.setTimeDischarge("8:20PM")
        p1.setReasonAdmission("Broken Arm")
        p1.addPrescription("Medicine 1", "15mg", "Every Morning")
        p1.addPrescription("Another Medicine", "3mg", "Every Night")
        p1.addScheduledProcedure("Surgery on leg at 3PM")
        p1.addScheduledProcedure("Another surgery at 5PM")
        p1.addDoctorNote("Patient needs medicine")
        p1.addDoctorNote("Patient is doing well")
        p1.addNurseNote("Patient had treatment at 7:15AM")
        p1.addNurseNote("Patient scheduled for surgery tomorrow")
        p1.setInsuranceCarrier("Big Insurance Company")
        p1.setInsuranceAccountNumber("123456789")
        p1.setInsuranceGroupNumber("987654")
        p1.setAmountPaid(481.1891024)
        p1.setAmountPaidByInsurance(15.81870)
        p1.addCharge("Broken leg repaired", 890.1333)
        p1.addCharge(
            "Really long charge name that would need to be wrapped around to display properly without going off of the screen",
            3101.31)
        p1.addCharge("Expensive Medicine administered", 443.145)
        self.patientList.append(p1)

        p = Patient()
        p.setFirstName("Richard")
        p.setLastname("jackson")
        p.setLocation(["Facility 3", "Floor 1", "Room 12", "Bed 2"])
        self.patientList.append(p)
        p = Patient()
        p.setFirstName("Amy")
        p.setLastname("Jones")
        p.setLocation(["Facility 1", "Floor 4", "Room 419", "Bed 1"])
        self.patientList.append(p)
        p = Patient()
        p.setFirstName("patrick")
        p.setLastname("burns")
        p.setLocation(["Facility 1", "Floor 3", "Room 363", "Bed 3"])
        self.patientList.append(p)
        p = Patient()
        p.setFirstName("My First Name")
        p.setLastname("MyLastName")
        p.setLocation(["My Facility", "My Floor", "My Room", "My Bed"])
        self.patientList.append(p)
        for i in range(20):
            first = "first " + str(i)
            last = "last " + str(i)
            location = "location " + str(i)
            p = Patient()
            p.setFirstName(first)
            p.setLastname(last)
            p.setLocation([location, "floor", "room", "bed"])
            self.patientList.append(p)


# create a system object to initialize TheSystem variable above
def initialize():
    system = System()


# Returns current master list of patients
def getPatientList():
    return System.TheSystem.patientList


def loadDatabase():
    # If database fails to load, load placeholder data instead
    try:
        patientCreator = Data.assignData.patientList()
        patientCreator.createList()
        System.TheSystem.patientList = patientCreator.getList()
    except:
        print("Loading placeholder data instead.")
        System.TheSystem.loadPlaceholderData()


# Returns the User object for the currently logged-in user
def getUser():
    return System.TheSystem.user


# Returns the type of the currently logged-in user
def getUserType():
    return System.TheSystem.user.getUserType()


def logoutUser():
    System.TheSystem.user = User()
    GUI.MainWindow.updateTopBar()  # update user type in TopBar
