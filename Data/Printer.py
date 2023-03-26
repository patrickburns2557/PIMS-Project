import Data.System
from Data.dataClasses import Patient
import GUI.MainWindow
import pandas as pd
from os import startfile
from datetime import datetime

#constant
REPORT_NAME = "PatientReport.txt"

# To use the class, simply call Data.Printer.initPrint() to print the current view

# This class allows a way to print patient data.
# First a user must add one or more patients with an add method
# Then they can use the print method to write the data to a text file.
class Printer():
    def __init__(self):
        self.patients = []
        self.viewType = None #set whenever view is switched

    #start printing the correct number of user(s)
    def startPrint(self):
        self.__getContext()
        if (self.viewType is None): # viewtype was not set yet.
            print("viewType not set!\nAborting print.")
            return
        elif self.viewType == 0:  # patient lists
            Printer.addPatients(self, Data.System.getPatientList())
            Printer.printPatients(self)
            return
        elif self.viewType == 1:  # todo: patient detailed view
            print("NOT IMPLEMENTED")
            return
        else:
            print("viewType unexpected value: " + str(self.viewType) + "\nAborting print.")
            return

    # are we printing one user or a whole list
    def __getContext(self):
        self.viewType = GUI.MainWindow.getViewType()
        print(self.viewType)


    # add a single patient to the list
    def addPatient(self, patient):
        # check if we are given the correct data type
        if type(patient) != Patient:
            print("Error: single patient expected. Found: " + str(type(patient)))
            return
        # add the patient
        self.patients.append(patient)

    # add multiple patients to the list at once using a list
    def addPatients(self, patients):
        # checks if we are given the correct data type
        if type(patients) != list:
            print("Error: list of patients expected. Found: " + str(type(patients)))
            return
        # add all the patients in the list
        for patient in patients:
            self.patients.append(patient)

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
        # write the data to a text file. Ensures all the data is shown and fits on one row
        with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.max_colwidth', None, 'display.expand_frame_repr', False):
            writeFile(df)

        #attempt to open the file in the default OS text editor
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
        f.write("PATIENT MANAGEMENT INFORMATION SYSTEM\nPatient Report(s) at "+str(datetime.now())+"\n")
        f.write(str(dataFrame))

    print("Printing complete! ")

#opens the report in the OS's text viewer
def openFile(file):
    startfile(file)

# print a current view
def initPrint():
    p=Printer()
    p.startPrint()