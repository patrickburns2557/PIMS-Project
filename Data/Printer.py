import Data.System
from Data.dataClasses import Patient
import GUI.MainWindow
import pandas as pd
from datetime import datetime
try:
    from os import startfile
except:
    #this library doesn't exist on linux
    pass

# constants
REPORT_NAME = "PatientReport.txt"

# To use the class, simply call Data.Printer.initPrint() to print the current view

# This class allows a way to print patient data.
# First a user must add one or more patients with an add method
# Then they can use the print method to write the data to a text file.
class Printer():
    def __init__(self):
        self.patients = []
        self.viewType = None  # set whenever view is switched

    # start printing the correct number of user(s)
    def startPrint(self, scope):
        self.__getContext()
        if (self.viewType is None):  # viewtype was not set yet.
            print("viewType not set!\nAborting print.")
            return
        elif self.viewType == 0:  # patient lists
            Printer.addPatients(self, Data.System.getPatientList())
            Printer.printPatients(self)
            return
        elif self.viewType == 1:
            Printer.addPatient(self, GUI.MainWindow.getCurrentPatient(), scope)
            Printer.printPatients(self)
            return
        else:
            print("viewType unexpected value: " + str(self.viewType) + "\nAborting print.")
            return

    # are we printing one user or a whole list
    def __getContext(self):
        self.viewType = GUI.MainWindow.getViewType()

    # add a single patient to the list.
    # If scope is provided, only print certain info: 0=all info, 1= personal, 2=medical, 3=Billing
    def addPatient(self, patient, scope):
        # check if we are given the correct data type
        if type(patient) != Patient:
            print("Error: single patient expected. Found: " + str(type(patient)))
            return

        # not all users should be able to view all info.
        redactedPatient = Patient()

        redactedPatient = addName(redactedPatient, patient)

        # only add info to redacted patient that a user is supposed to view
        ut = Data.System.getUserType()
        if ut == 0 or ut == 1:  # doctors & nurses should access everything
            if scope == 0 or scope == 1:  # personal info
                redactedPatient = addPersonalInfo(redactedPatient, patient)
            if scope == 0 or scope == 2:  # medical info
                redactedPatient = addMedicalInfo(redactedPatient, patient)
            if scope == 0 or scope == 3:  # billing info
                redactedPatient = addBillingInfo(redactedPatient, patient)

        elif ut == 2:  # office staff
            if scope == 0 or scope == 1:  # personal info
                redactedPatient = addPersonalInfo(redactedPatient, patient)
            if scope == 0 or scope == 3:  # billing info
                redactedPatient = addBillingInfo(redactedPatient, patient)

        elif ut == 3:  # volunteer
            if scope == 0 or scope == 1:  # personal info
                redactedPatient = addPersonalInfo(redactedPatient, patient)

        else:
            print("Unknown user type" + str(ut) + ". Aborting print!")
            return

        # add the patient
        self.patients.append(redactedPatient)

    # add multiple patients to the list at once using a list
    def addPatients(self, patients):
        # checks if we are given the correct data type
        if type(patients) != list:
            print("Error: list of patients expected. Found: " + str(type(patients)))
            return

        # check if user is doctor, nurse, staff, volunteer
        ut = Data.System.getUserType()
        # add all the patients in the list
        for patient in patients:
            redactedPatient = Patient()
            redactedPatient = addName(redactedPatient, patient)  # everyone is allowed the name

            # check privileges
            if ut == 0 or ut == 1:  # doctor or nurse
                redactedPatient = addPersonalInfo(redactedPatient, patient)
                redactedPatient = addMedicalInfo(redactedPatient, patient)
                redactedPatient = addBillingInfo(redactedPatient, patient)
            elif ut == 2:  # office staff
                redactedPatient = addPersonalInfo(redactedPatient, patient)
                redactedPatient = addBillingInfo(redactedPatient, patient)
            elif ut == 3:  # volunteer
                redactedPatient = addPersonalInfo(redactedPatient, patient)
            else:
                print("Unknown usertype " + str(ut) + " Aborting print!")
                return

            self.patients.append(redactedPatient)

    # output patients
    def printPatients(self):
        # check if any patients have been added yet. If none, print an error and quit.
        if len(self.patients) == 0:
            print("Print Error: No patients found!")
            return
        # format patient data in a readable way
        df = makeDataFrame(self.patients)
        if df.empty:
            return

        # order the dataframe in a sensible manner
        df = df[[
            'firstName', 'middleName', 'lastName',
            'address',
            'homePhone', 'workPhone', 'mobilePhone',
            'emergencyContactNames', 'emergencyContactNumbers',
            'dateAdmittance', 'timeAdmittance',
            'reasonAdmission',
            'dateDischarge', 'timeDischarge',
            'familyDoctor',
            'doctorNotes', 'nurseNotes',
            'prescriptionNames', 'prescriptionSchedule', 'prescriptionAmount',
            'scheduledProcedures',
            'location',
            'numAllowedVisitors', 'allowedVisitors',
            'insuranceCarrier', 'insuranceAccountNumber', 'insuranceGroupNumber',
            'listCharges', 'listChargesAmount',
            'amountPaid', 'amountOwed', 'amountPaidByInsurance'
        ]]
        # write the data to a text file. Ensures all the data is shown and fits on one row
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None,
                               'display.expand_frame_repr', False):
            writeFile(df)

        # attempt to open the file in the default OS text editor
        try:
            openFile(REPORT_NAME)
        except:
            print("Could not automatically open report.")


# create a data frame given a list of patients
def makeDataFrame(patients):
    # get all members (variable names) of an object
    members = []
    for patient in patients:
        members = [attr for attr in dir(patient) if
                   not callable(getattr(patient, attr)) and not attr.startswith("__")]
    if len(members) == 0:
        print("No members!")
        return None

    # creates a 2d array where the rows are each patient and the columns are the patient's data
    table = [[getattr(patients[i], members[j]) for j in range(0, len(members))] for i in range(0, len(patients))]

    # use pandas to create a neatly formatted table
    df = pd.DataFrame(table, columns=members)
    return df


# writes a dataframe to a text file
def writeFile(dataFrame):
    with open(REPORT_NAME, 'w') as f:
        f.write("PATIENT MANAGEMENT INFORMATION SYSTEM\nPatient Report(s) at " + str(datetime.now()) + "\n\n")
        f.write(str(dataFrame))

    print("Printing complete! ")


# opens the report in the OS's text viewer
def openFile(file):
    try:
        startfile(file)
    except:
        #This library doesn't exist on linux
        pass


# print a current view
def initPrint(scope):
    p = Printer()
    p.startPrint(scope)


# add full name to redactedPatient
def addName(redactedPatient, patient):
    # everyone is allowed the name of patient
    redactedPatient.setFirstName(patient.firstName)
    redactedPatient.setMiddleName(patient.middleName)
    redactedPatient.setLastname(patient.lastName)

    return redactedPatient


# add all personal info to redactedPatient
def addPersonalInfo(redactedPatient, patient):
    # name
    redactedPatient = addName(redactedPatient, patient)

    # address
    redactedPatient.setAddress(patient.address)
    redactedPatient.setLocation(patient.location)

    # phone
    redactedPatient.setMobilePhone(patient.mobilePhone)
    redactedPatient.setHomePhone(patient.homePhone)
    redactedPatient.setWorkPhone(patient.workPhone)

    for e in range(0, len(patient.emergencyContactNames)):
        redactedPatient.addEmergencyContact(patient.emergencyContactNames[e],
                                            patient.emergencyContactNumbers[e])

    # visitors
    redactedPatient.setNumAllowedVisitors(patient.allowedVisitors)
    for v in patient.allowedVisitors:
        redactedPatient.addAllowedVisitor(v)

    return redactedPatient


# add med info to redactedPatient
def addMedicalInfo(redactedPatient, patient):
    redactedPatient.setFamilyDoctor(patient.familyDoctor)

    redactedPatient.setDateAdmittance(patient.dateAdmittance)
    redactedPatient.setTimeAdmittance(patient.dateAdmittance)
    redactedPatient.setReasonAdmission(patient.reasonAdmission)

    # discharge
    redactedPatient.setDateDischarge(patient.dateDischarge)
    redactedPatient.setTimeDischarge(patient.timeDischarge)

    # prescriptions
    for p in range(0, len(patient.prescriptionNames)):
        redactedPatient.addPrescription(patient.prescriptionNames[p], patient.prescriptionAmount[p],
                                        patient.prescriptionSchedule[p])
    # scheduled procedures
    for s in patient.scheduledProcedures:
        redactedPatient.addScheduledProcedure(s)

    for n in patient.doctorNotes:
        redactedPatient.addDoctorNote(n)

    for n in patient.nurseNotes:
        redactedPatient.addNurseNote(n)
    return redactedPatient


# add billing info to redactedPatient
def addBillingInfo(redactedPatient, patient):
    # insurance info
    redactedPatient.setAmountPaidByInsurance(patient.amountPaidByInsurance)
    redactedPatient.setInsuranceCarrier(patient.insuranceCarrier)
    redactedPatient.setInsuranceGroupNumber(patient.insuranceGroupNumber)
    redactedPatient.setInsuranceAccountNumber(patient.insuranceAccountNumber)

    # billing info
    redactedPatient.setAmountPaid(patient.amountPaid)
    redactedPatient.setAmountOwed(patient.amountOwed)

    # list of charges
    for c in range(0, len(patient.listCharges)):
        redactedPatient.addCharge(patient.listCharges[c], patient.listChargesAmount[c])

    return redactedPatient
