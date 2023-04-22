import Data.addNewInfo

# class to ensure all information entered in add/edit patient is valid


class validateInfo():

    def __init__(self):

       self.issue = ""

    def checkEntry(self, patient):
        
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

        elif len(patient.emergencyContactNames[0]) > 50:
            self.issue = "Emergency contact 1 name exceeds character limit."

        elif len(patient.emergencyContactNames[1]) > 50:
            self.issue = "Emergency contact 2 name exceeds character limit."

        elif len(patient.emergencyContactNumbers[0]) > 20:
            self.issue = "Emergency contact 1 number exceeds character limit."

        elif len(patient.emergencyContactNames[1]) > 20:
            self.issue = "Emergency contact 2 number exceeds character limit."

        elif len(patient.numAllowedVisitors) > 3:
            self.issue = "Max simultaneous visitors exceeds character limit."

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


    
    # if no issues found in info, add to database and return true
    def checkValidity(self, patient, new):
        if self.issue == "":
            if new == True:
                Data.addNewInfo.addNewInfo().updatePatient(patient, True)
            else:
                Data.addNewInfo.addNewInfo().updatePatient(patient, False)
            return True
        
        else:
            return False
        

    def checkIssue(self):
        return self.issue