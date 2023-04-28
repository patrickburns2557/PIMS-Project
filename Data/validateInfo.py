import Data.addNewInfo
import re

# class to ensure all information entered in add/edit patient is valid


class validateInfo():

    def __init__(self):

       self.issue = ""

    def checkEntry(self, patient):

        # check character length of incoming values
        
        if len(patient.firstName) > 20:
            self.issue = "First name exceeds character limit."
        
        elif len(patient.middleName) > 20:
            self.issue = "Middle name exceeds character limit."
        
        elif len(patient.lastName) > 20:
            self.issue = "Last name exceeds character limit."

        elif len(patient.address[0]) > 50:
            self.issue = "Street name exceeds character limit."
        
        elif len(patient.address[1]) > 20:
            self.issue = "City exceeds character limit."

        elif len(patient.address[2]) > 20:
            self.issue = "State exceeds character limit."

        elif len(patient.address[3]) > 20:
            self.issue = "Zip code exceeds character limit."

        elif len(patient.location[0]) > 20:
            self.issue = "Facility name exceeds character limit."

        elif len(patient.location[1]) > 10:
            self.issue = "Floor number exceeds character limit."

        elif len(patient.location[2]) > 10:
            self.issue = "Room number exceeds character limit."

        elif len(patient.location[3]) > 10:
            self.issue = "Bed number exceeds character limit."

        elif len(patient.emergencyContactNames) >= 1 and len(patient.emergencyContactNames[0]) > 50:
            self.issue = "Emergency contact 1 name exceeds character limit"

        elif len(patient.emergencyContactNames) >= 2 and len(patient.emergencyContactNames[1]) > 50:
            self.issue = "Emergency contact 2 name exceeds character limit"

        elif len(patient.emergencyContactNames) == 3 and len(patient.emergencyContactNames[2]) > 50:
            self.issue = "Emergency contact 3 name exceeds character limit"

        elif len(patient.emergencyContactNumbers) >= 1 and len(patient.emergencyContactNumbers[0]) > 20:
            self.issue = "Emergency contact 1 number exceeds character limit"

        elif len(patient.emergencyContactNumbers) >= 2 and len(patient.emergencyContactNumbers[1]) > 20:
            self.issue = "Emergency contact 2 number exceeds character limit"

        elif len(patient.emergencyContactNumbers) == 3 and len(patient.emergencyContactNumbers[2]) > 20:
            self.issue = "Emergency contact 3 number exceeds character limit"

        elif len(patient.numAllowedVisitors) > 3:
            self.issue = "Max simultaneous visitors exceeds character limit."

        elif len(patient.numAllowedVisitors) > 0:
            for num in patient.numAllowedVisitors:
                amount = ord(num)
                if amount < 48 or amount > 57:
                    self.issue = "Invalid entry for max simulataneous visitors."
                

        elif len(patient.mobilePhone) > 20:
            self.issue = "Mobile phone number exceeds character limit."

        elif len(patient.homePhone) > 20:
            self.issue = "Home phone number exceeds character limit."

        elif len(patient.workPhone) > 20:
            self.issue = "Work phone number exceeds character limit."

        elif len(patient.insuranceCarrier) > 50:
            self.issue = "Insurance carrier exceeds character limit."

        elif len(patient.insuranceAccountNumber) > 20:
            self.issue = "Insurance account number exceeds character limit."

        elif len(patient.insuranceGroupNumber) > 20:
            self.issue = "Insurance group number exceeds character limit."

        # make sure no letters or invalid symbols are entered for phone numbers

        if len(patient.emergencyContactNumbers) != 0 and patient.emergencyContactNumbers[0] != "":
            check = re.search("^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", patient.emergencyContactNumbers[0])
            if check == None:
                self.issue = "Invalid entry for emergency number 1"

        if len(patient.emergencyContactNumbers) >= 2 and patient.emergencyContactNumbers[1] != "":
            check = re.search("^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", patient.emergencyContactNumbers[1])
            if check == None:
                self.issue = "Invalid entry for emergency number 2"

        if len(patient.emergencyContactNumbers) >= 3 and patient.emergencyContactNumbers[2] != "":
            check = re.search("^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", patient.emergencyContactNumbers[2])
            if check == None:
                self.issue = "Invalid entry for emergency number 3"

        if patient.mobilePhone != "":
            check = re.search("^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", patient.mobilePhone)
            if check == None:
                self.issue = "Invalid entry for mobile phone number"

        if patient.homePhone != "":
            check = re.search("^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", patient.homePhone)
            if check == None:
                self.issue = "Invalid entry for home phone number"

        if patient.workPhone != "":
            check = re.search("^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$", patient.workPhone)
            if check == None:
                self.issue = "Invalid entry for work phone number"

    # if no issues found in info, add to database and return true
    def checkValidity(self, patient, new):
        if self.issue == "":
            if new == True:
                # add new patient to database
                try:
                    Data.addNewInfo.addNewInfo().updatePatient(patient, True)
                except:
                    pass
            else:
                # update existing patient
                try:
                    Data.addNewInfo.addNewInfo().updatePatient(patient, False)
                except:
                    pass

            return True, self.issue
        
        else:
            return False, self.issue