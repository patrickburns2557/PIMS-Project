#classes for the program
#Users, patients, login, etc...
#we may want to split this up further

class Patient():
    def __init__(self):
        
        #PERSONAL INFORMATION
        self.firstName = ""
        self.middleName = ""
        self.lastName = ""
        self.address = ["", "", "", ""] # Street, City, State, Zip
        self.homePhone = ""
        self.workPhone = ""
        self.mobilePhone = ""
        self.emergencyContactNames = [] # Name, Phone number
        self.emergencyContactNumbers = [] # Phone number of emergency contact
        
        
        #MEDICAL INFORMATION
        self.dateAdmittance = ""
        self.timeAdmittance = ""
        self.reasonAdmission = ""
        self.familyDoctor = ""
        self.dateDischarge = ""
        self.timeDischarge = ""
        self.doctorNotes = [] # List of strings to append to
        self.nurseNotes = [] # List of strings to append to
        self.prescriptionNames = [] # List of strings to append to
        self.prescriptionAmount = [] # List of strings to append to
        self.prescriptionSchedule = [] # List of strings to append to
        self.scheduledProcedures = [] # List of strings to append to
        

        #LOCATION INFORMATION
        self.location = ["", "", "", ""] # Facility, Floor, Room, Bed number
        self.locationFacility = ""
        self.locationFloor = ""
        self.locationRoom = ""
        self.locationBed = "" # Bed number in a given room
        self.numAllowedVisitors = ""
        self.allowedVisitors = [] # List of visitor names


        #BILLING INFORMATION
        self.insuranceCarrier = ""
        self.insuranceAccountNumber = ""
        self.insuranceGroupNumber = ""
        self.listCharges = [] # List of strings containing the name of each charge
        self.listChargesAmount = [] # List of floats(?) containing the value of each charge
        self.amountPaid = 0.0
        self.amountOwed = 0.0
        self.amountPaidByInsurance = 0.0

    
    ################################
    # PERSONAL INFORMATION METHODS
    ################################
    def setFirstName(self, firstName):
        self.firstName = firstName
    
    def setMiddleName(self, middleName):
        self.middleName = middleName

    def setLastname(self, lastName):
        self.lastName = lastName

    # address = list of 4 strings that equate to Street, City, State, Zip
    def setAddress(self, address):
        self.address[0] = address[0] # Street
        self.address[1] = address[1] # City
        self.address[2] = address[2] # State
        self.address[3] = address[3] # Zip
    
    def setHomePhone(self, homePhone):
        self.homePhone = homePhone

    def setWorkPhone(self, workPhone):
        self.workPhone = workPhone

    def setMobilePhone(self, mobilePhone):
        self.mobilePhone = mobilePhone
    
    def addEmergencyContact(self, emergencyContactName, emergencyContactNumber):
        self.emergencyContactNames.append(emergencyContactName)
        self.emergencyContactNumbers.append(emergencyContactNumber)
    

    ################################
    # MEDICAL INFORMATION METHODS
    ################################
    def setDateAdmittance(self, dateAdmittance):
        self.dateAdmittance = dateAdmittance

    def setTimeAdmittance(self, timeAdmittance):
        self.timeAdmittance = timeAdmittance

    def setReasonAdmission(self, reasonAdmission):
        self.reasonAdmission = reasonAdmission

    def setFamilyDoctor(self, familyDoctor):
        self.familyDoctor = familyDoctor
    
    def setDateDischarge(self, dateDischarge):
        self.dateDischarge = dateDischarge

    def setTimeDischarge(self, timeDischarge):
        self.timeDischarge = timeDischarge

    def addDoctorNote(self, doctorNote):
        self.doctorNotes.append(doctorNote)

    def addNurseNote(self, nurseNote):
        self.nurseNotes.append(nurseNote)

    def addPrescription(self, prescriptionName, prescriptionAmount, prescriptionSchedule):
        self.prescriptionNames.append(prescriptionName)
        self.prescriptionAmount.append(prescriptionAmount)
        self.prescriptionSchedule.append(prescriptionSchedule)

    def addScheduledProcedure(self, scheduledProcedure):
        self.scheduledProcedures.append(scheduledProcedure)

    
    ################################
    # LOCATION INFORMATION METHODS
    ################################
    # location = list of 4 strings that equate to Facility, Floor, Room number, and Bed number
    def setLocation(self, location):
        self.location[0] = location[0] # Facility
        self.location[1] = location[1] # Floor
        self.location[2] = location[2] # Room number
        self.location[3] = location[3] # Bed number

    def setNumAllowedVisitors(self, numVisitors):
        self.numAllowedVisitors = numVisitors

    def addAllowedVisitor(self, allowedVisitor):
        self.allowedVisitors.append(allowedVisitor)
    

    ################################
    # BILLING INFORMATION METHODS
    ################################
    def setInsuranceCarrier(self, insuranceCarrier):
        self.insuranceCarrier = insuranceCarrier

    def setInsuranceAccountNumber(self, accountNumber):
        self.insuranceAccountNumber = accountNumber

    def setInsuranceGroupNumber(self, groupNumber):
        self.insuranceGroupNumber = groupNumber

    def addCharge(self, charge, chargeAmount):
        self.listCharges.append(charge)
        self.listChargesAmount.append(chargeAmount)

    def setAmountPaid(self, amountPaid):
        self.amountPaid = amountPaid

    def setAmountOwed(self, amountOwed):
        self.amountOwed = amountOwed
    
    def updateAmountOwed(self):
        totalCharges = 0.0
        for x in self.listChargesAmount:
            totalCharges += x
        self.amountOwed = totalCharges - self.amountPaid - self.amountPaidByInsurance

    def setAmountPaidByInsurance(self, amount):
        self.amountPaidByInsurance = amount

class User:
    def __init__(self):
        self.userType = 0
        self.username = ""
        self.password = ""
        