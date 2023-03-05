#create list of patient objects from database info

import sqlConnector
from dataClasses import Patient

# open database for use
db = sqlConnector.myConnector()
db.execute("use patient_information;")

# add columns for allowed visitors amount and names 
# db.addColumn("allowed_visitor_amount")
# db.addColumn("allowed_visitor_names")

# add number and name of allowed visitors to all patients
db.update("allowed_visitor_amount", "1", "0")
db.update("allowed_visitor_amount", "3", "1")
db.update("allowed_visitor_amount", "1", "2")
db.update("allowed_visitor_amount", "2", "3")
db.update("allowed_visitor_amount", "4", "4")
db.update("allowed_visitor_amount", "3", "5")
db.update("allowed_visitor_amount", "1", "6")
db.update("allowed_visitor_amount", "2", "7")
db.update("allowed_visitor_amount", "3", "8")
db.update("allowed_visitor_amount", "4", "9")

db.update("allowed_visitor_names", "'Vivian Garcia'", "0")
db.update("allowed_visitor_names", "'Jaxon Patel\nOmar Lucero\nJada Thompson'", "1")
db.update("allowed_visitor_names", "'Kyle Nguyen'", "2")
db.update("allowed_visitor_names", "'Robert Smith\nAlex Smith'", "3")
db.update("allowed_visitor_names", "'Lilith Carter\nNixon Lainey\nLily Chen\nXavier Davis'", "4")
db.update("allowed_visitor_names", "'Blaine Brown\nBlaze Rojas\nNathan Kim'", "5")
db.update("allowed_visitor_names", "'Skyla Williams'", "6")
db.update("allowed_visitor_names", "'Tristan Davis\nAbby Davis'", "7")
db.update("allowed_visitor_names", "'Heidi Rodriguez\nAndrew Rodriguez\nSarah Lee'", "8")
db.update("allowed_visitor_names", "'Ryan Herring\nLila Fitzpatrick\nOlivia White\nEthan Johnson'", "9")



# method to get specific data from database by column
def setData(data):
    s = "SELECT " + data + " FROM patient_info;"
    db.execute(s)
    x = db.fetch()
    return x

class patientList():

    def __init__(self):

        # open database for use
        db = sqlConnector.myConnector()
        db.execute("use patient_information;")
        self.patientRecords = []

    def createList(self):
        for i in range(10):

            patients = Patient()

            # getting personal info
            patients.setFirstName((setData("first_name")[i])[0])
            patients.setLastname((setData("last_name")[i])[0])
            patients.setMiddleName((setData("middle_name")[i])[0])

            address = []
            address.append((setData("adress_street")[i])[0])
            address.append((setData("address_city")[i])[0])
            address.append((setData("address_state")[i])[0])
            address.append((setData("address_zip")[i])[0])
            patients.setAddress(address)

            patients.setHomePhone((setData("home_phone")[i])[0])
            patients.setWorkPhone((setData("work_phone")[i])[0])
            patients.setMobilePhone((setData("mobile_phone")[i])[0])

            patients.addEmergencyContact((setData("emergency1_first_name")[i][0]), (setData("emergency1_number")[i][0]))
            patients.addEmergencyContact((setData("emergency2_first_name")[i][0]), (setData("emergency2_number")[i][0]))

            # getting medical info

            patients.setDateAdmittance((setData("date_of_admittance")[i][0]))
            patients.setTimeAdmittance((setData("time_of_admittance")[i][0]))
            patients.setReasonAdmission((setData("reason_for_admission")[i][0]))

            patients.setFamilyDoctor((setData("family_doctor")[i][0]))
            patients.dateDischarge = ((setData("discharge_date")[i])[0])
            patients.timeDischarge = ((setData("discharge_time")[i])[0])

            patients.addDoctorNote((setData("doctor_treatment_notes")[i][0]))
            patients.addNurseNote((setData("nurse_treatment_notes")[i][0]))

            prescriptionName = (setData("prescription_name")[i][0]).split('\n')
            prescriptionAmounts = (setData("prescription_amount")[i][0]).split('\n')
            prescriptionTime = (setData("prescription_schedule")[i][0]).split('\n')

            for j in range(len(prescriptionName)):
                patients.addPrescription(prescriptionName[j], prescriptionAmounts[j], prescriptionTime[j])

            procedures = (setData("scheduled_procedures")[i][0]).split('\n')

            for j in range(len(procedures)):
                patients.addScheduledProcedure(procedures[j])

            # getting location info

            location = []
            location.append((setData("facility_name")[i])[0])
            location.append((setData("floor_number")[i])[0])
            location.append((setData("room_number")[i])[0])
            location.append((setData("bed_number")[i])[0])
            patients.setLocation(location)

            patients.setNumAllowedVisitors((setData("allowed_visitor_amount")[i])[0])
            visitors = (setData("allowed_visitor_names")[i][0]).split('\n')
            num = int(patients.numAllowedVisitors)

            for j in range(num):
                patients.addAllowedVisitor(visitors[j])

            patients.setInsuranceCarrier((setData("insurace_carrier")[i])[0])
            patients.setInsuranceAccountNumber((setData("insurance_account_number")[i])[0])
            patients.setInsuranceGroupNumber((setData("insurance_group_number")[i])[0])

            # getting billing info

            charges = (setData("billing_items")[i][0]).split('\n')
            for c in charges:
                amount = ""
                name = ""
                for letter in c:
                    if letter.isdigit():
                        amount = amount + letter
                    elif letter.isalpha():
                        name = name + letter
                    
                amount = float(amount)
                patients.addCharge(name, amount)

                patients.setAmountOwed((setData("amound_owed")[i])[0])
                patients.setAmountPaid((setData("amount_paid")[i])[0])
                patients.setAmountPaidByInsurance((setData("paid_by_insurance")[i])[0])

            # list of all patient objects
            self.patientRecords.append(patients)