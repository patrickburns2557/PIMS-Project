# create list of patient objects from database info
import Data.System
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

        # get user type
        userType = Data.System.getUserType()

        for i in range(rowCount):

            patients = Patient()

            # information that all login types can view

            try:
                # patient name and id
                patients.setID((setData("patient_ID")[i][0]))
                patients.setFirstName((setData("first_name")[i])[0])
                patients.setLastname((setData("last_name")[i])[0])
                patients.setMiddleName((setData("middle_name")[i])[0])

                # location
                location = []
                location.append((setData("facility_name")[i])[0])
                location.append((setData("floor_number")[i])[0])
                location.append((setData("room_number")[i])[0])
                location.append((setData("bed_number")[i])[0])
                patients.setLocation(location)

                # emergency contacts
                if (setData("emergency1_name")[i][0]) != None and (setData("emergency1_number")[i][0]) != None:
                    patients.addEmergencyContact((setData("emergency1_name")[i][0]), (setData("emergency1_number")[i][0]))
                if (setData("emergency2_name")[i][0]) != None and (setData("emergency2_number")[i][0]) != None:
                    patients.addEmergencyContact((setData("emergency2_name")[i][0]), (setData("emergency2_number")[i][0]))
                if (setData("emergency3_name")[i][0]) != None and (setData("emergency3_number")[i][0]) != None:
                    patients.addEmergencyContact((setData("emergency3_name")[i][0]), (setData("emergency3_number")[i][0]))

                # allowed visitor amount and names
                patients.setNumAllowedVisitors((setData("allowed_visitor_amount")[i])[0])
                visitors = (setData("allowed_visitor_names")[i][0]).split('\n')

                if len(visitors) != 0:
                    for visitor in visitors:
                        patients.addAllowedVisitor(visitor)

                # information that everyone but volunteers may access
                if userType == 0 or userType == 1 or userType == 2:

                    # address
                    address = []
                    address.append((setData("address_street")[i])[0])
                    address.append((setData("address_city")[i])[0])
                    address.append((setData("address_state")[i])[0])
                    address.append((setData("address_zip")[i])[0])
                    patients.setAddress(address)

                    # phone numbers
                    patients.setHomePhone((setData("home_phone")[i])[0])
                    patients.setWorkPhone((setData("work_phone")[i])[0])
                    patients.setMobilePhone((setData("mobile_phone")[i])[0])

                    # insurance information
                    patients.setInsuranceCarrier((setData("insurance_carrier")[i])[0])
                    patients.setInsuranceAccountNumber((setData("insurance_account_number")[i])[0])
                    patients.setInsuranceGroupNumber((setData("insurance_group_number")[i])[0])


                    # billing info
                    names = (setData("billing_items_name")[i][0]).split('\n')
                    amounts = (setData("billing_items_amount")[i][0]).split('\n')

                    if len(names) != 0 and len(amounts) != 0:
                        for j in range(len(names)):
                            amounts[j] = float(amounts[j])
                            patients.addCharge(names[j], amounts[j])

                    patients.setAmountOwed(float((setData("amount_owed")[i])[0]))
                    patients.setAmountPaid(float((setData("amount_paid")[i])[0]))
                    patients.setAmountPaidByInsurance(float((setData("paid_by_insurance")[i])[0]))

                # information that only doctors and nurses may view
                if userType == 0 or userType == 1:

                    # admission info

                    patients.setDateAdmittance((setData("date_of_admittance")[i][0]))
                    patients.setTimeAdmittance((setData("time_of_admittance")[i][0]))
                    patients.setReasonAdmission((setData("reason_for_admission")[i][0]))

                    # discharge info

                    patients.setFamilyDoctor((setData("family_doctor")[i][0]))
                    patients.dateDischarge = ((setData("discharge_date")[i])[0])
                    patients.timeDischarge = ((setData("discharge_time")[i])[0])

                    # treatment notes

                    doctorNotes = (setData("doctor_treatment_notes")[i][0]).split('\n')
                    nurseNotes = (setData("nurse_treatment_notes")[i][0]).split('\n')

                    if len(doctorNotes) != 0:
                        for note in range(len(doctorNotes)):
                            patients.addDoctorNote(doctorNotes[note])

                    if len(nurseNotes) != 0:
                        for note in range(len(nurseNotes)):
                            patients.addNurseNote(nurseNotes[note])

                    # prescription info

                    prescriptionName = (setData("prescription_name")[i][0]).split('\n')
                    prescriptionAmounts = (setData("prescription_amount")[i][0]).split('\n')
                    prescriptionTime = (setData("prescription_schedule")[i][0]).split('\n')

                    if len(prescriptionName) != 0 and len(prescriptionAmounts) != 0 and len(prescriptionTime) != 0:
                        for j in range(len(prescriptionName)):
                            patients.addPrescription(prescriptionName[j], prescriptionAmounts[j], prescriptionTime[j])

                    # schedules procedures info

                    procedures = (setData("scheduled_procedures")[i][0]).split(', ')

                    if len(procedures) != 0:
                        for j in range(len(procedures)):
                            patients.addScheduledProcedure(procedures[j])


                # list of all patient objects
                self.patientRecords.append(patients)

            except:
                pass

    # returns completed list of patient objects
    def getList(self):
        return self.patientRecords