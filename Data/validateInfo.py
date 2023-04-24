import Data.addNewInfo

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

        if len(patient.emergencyContactNumbers) != 0:
            for num in patient.emergencyContactNumbers[0]:
                num = ord(num) 
                if (num < 48 or num > 57) and (num != 40 and num != 41 and num != 45):
                    self.issue = "Invalid entry for emergency number 1"
                    break

        if len(patient.emergencyContactNumbers) == 2:
            for num in patient.emergencyContactNumbers[1]:
                num = ord(num) 
                if (num < 48 or num > 57) and (num != 40 and num != 41 and num != 45):
                    self.issue = "Invalid entry for emergency number 2"
                    break

        if len(patient.emergencyContactNumbers) == 3:
            for num in patient.emergencyContactNumbers[2]:
                num = ord(num) 
                if (num < 48 or num > 57) and (num != 40 and num != 41 and num != 45):
                    self.issue = "Invalid entry for emergency number 3"
                    break

        for num in patient.mobilePhone:
            num = ord(num) 
            if (num < 48 or num > 57) and (num != 40 and num != 41 and num != 45):
                self.issue = "Invalid entry for mobile phone number"
                break

        for num in patient.homePhone:
            num = ord(num) 
            if (num < 48 or num > 57) and (num != 40 and num != 41 and num != 45):
                self.issue = "Invalid entry for home phone number"
                break

        for num in patient.workPhone:
            num = ord(num) 
            if (num < 48 or num > 57) and (num != 40 and num != 41 and num != 45):
                self.issue = "Invalid entry for work phone number"
                break

    # if no issues found in info, add to database and return true
    def checkValidity(self, patient, new):
        if self.issue == "":
            if new == True:
                # add new patient to database
                Data.addNewInfo.addNewInfo().updatePatient(patient, True)
            else:
                # update existing patient
                Data.addNewInfo.addNewInfo().updatePatient(patient, False)
            return True, self.issue
        
        else:
            return False, self.issue