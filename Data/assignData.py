# create list of patient objects from database info
 
from Data.sqlConnector import *
from Data.dataClasses import *

# access database
db = myConnector()

# method to get specific data from database by column
def setData(data):
    s = "SELECT " + data + " FROM patients;"
    db.execute(s)
    x = db.fetch()
    return x

class patientList():

    def __init__(self):

        # list of patient objects
        self.patientRecords = []

    def createList(self):

        # get current amount of patients
        rowCount = db.checkRowCount()

        for i in range(rowCount):

            patients = Patient()

            # getting personal info
            patients.setFirstName((setData("first_name")[i])[0])
            patients.setLastname((setData("last_name")[i])[0])
            patients.setMiddleName((setData("middle_name")[i])[0])

            address = []
            address.append((setData("address_street")[i])[0])
            address.append((setData("address_city")[i])[0])
            address.append((setData("address_state")[i])[0])
            address.append((setData("address_zip")[i])[0])
            patients.setAddress(address)

            patients.setHomePhone((setData("home_phone")[i])[0])
            patients.setWorkPhone((setData("work_phone")[i])[0])
            patients.setMobilePhone((setData("mobile_phone")[i])[0])

            patients.addEmergencyContact((setData("emergency1_name")[i][0]), (setData("emergency1_number")[i][0]))
            patients.addEmergencyContact((setData("emergency2_name")[i][0]), (setData("emergency2_number")[i][0]))

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

            procedures = (setData("scheduled_procedures")[i][0]).split(', ')

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

            patients.setInsuranceCarrier((setData("insurance_carrier")[i])[0])
            patients.setInsuranceAccountNumber((setData("insurance_account_number")[i])[0])
            patients.setInsuranceGroupNumber((setData("insurance_group_number")[i])[0])

            # getting billing info

            names = (setData("billing_items_name")[i][0]).split('\n')
            amounts = (setData("billing_items_amount")[i][0]).split('\n')

            for j in range(len(names)):
                amounts[j] = float(amounts[j])
                patients.addCharge(names[j], amounts[j])

            patients.setAmountOwed((setData("amount_owed")[i])[0])
            patients.setAmountPaid((setData("amount_paid")[i])[0])
            patients.setAmountPaidByInsurance((setData("paid_by_insurance")[i])[0])

            # list of all patient objects
            self.patientRecords.append(patients)

    # returns completed list of patient objects
    def getList(self):
        return self.patientRecords