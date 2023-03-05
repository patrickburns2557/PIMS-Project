from Data.dataClasses import Patient
import pandas as pd

# This class allows a way to print patient data.
# First a user must add one or more patients with an add method
# Then they can use the print method to write the data to a text file.
class Printer():
    def __init__(self):
        self.patients = []

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
        # write the data to a text file
        writeFile(df)


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
    with open('patientReport.txt', 'w') as f:
        f.write("Patient Management Information System\nPatient Report:\n")
        f.write(str(dataFrame))

    print("Printing complete! ")