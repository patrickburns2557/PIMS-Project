# create list of patient objects from database info
import Data.System
from Data.sqlConnector import *
from Data.dataClasses import *


class patientList:

    def __init__(self):

        # access database
        self.db = myConnector()

        # list of patient objects
        self.patientRecords = []

    # method to get specific data from database by column
    def setData(self, data):
        s = "SELECT " + data + " FROM patients;"
        self.db.execute(s)
        x = self.db.fetch()
        return x

    def createList(self):

        # get current amount of patients
        rowCount = self.db.checkRowCount()

        # get user type
        userType = Data.System.getUserType()

        for i in range(rowCount):

            patients = Patient()

            # information that all login types can view

            try:
                # patient name and id
                patients.setID((self.setData("patient_ID")[i][0]))
                patients.setFirstName((self.setData("first_name")[i])[0])
                patients.setLastname((self.setData("last_name")[i])[0])
                patients.setMiddleName((self.setData("middle_name")[i])[0])

                # location
                location = []
                location.append((self.setData("facility_name")[i])[0])
                location.append((self.setData("floor_number")[i])[0])
                location.append((self.setData("room_number")[i])[0])
                location.append((self.setData("bed_number")[i])[0])
                patients.setLocation(location)

                # emergency contacts
                if (self.setData("emergency1_name")[i][0]) is not None and (
                        self.setData("emergency1_number")[i][0]) is not None:
                    patients.addEmergencyContact((self.setData("emergency1_name")[i][0]),
                                                 (self.setData("emergency1_number")[i][0]))
                if (self.setData("emergency2_name")[i][0]) is not None and (
                        self.setData("emergency2_number")[i][0]) is not None:
                    patients.addEmergencyContact((self.setData("emergency2_name")[i][0]),
                                                 (self.setData("emergency2_number")[i][0]))
                if (self.setData("emergency3_name")[i][0]) is not None and (
                        self.setData("emergency3_number")[i][0]) is not None:
                    patients.addEmergencyContact((self.setData("emergency3_name")[i][0]),
                                                 (self.setData("emergency3_number")[i][0]))

                # allowed visitor amount and names
                patients.setNumAllowedVisitors((self.setData("allowed_visitor_amount")[i])[0])
                visitors = (self.setData("allowed_visitor_names")[i][0]).split('\n')

                if len(visitors) != 0:
                    for visitor in visitors:
                        patients.addAllowedVisitor(visitor)

                # information that everyone but volunteers may access
                if userType == 0 or userType == 1 or userType == 2:

                    # address
                    address = []
                    address.append((self.setData("address_street")[i])[0])
                    address.append((self.setData("address_city")[i])[0])
                    address.append((self.setData("address_state")[i])[0])
                    address.append((self.setData("address_zip")[i])[0])
                    patients.setAddress(address)

                    # phone numbers
                    patients.setHomePhone((self.setData("home_phone")[i])[0])
                    patients.setWorkPhone((self.setData("work_phone")[i])[0])
                    patients.setMobilePhone((self.setData("mobile_phone")[i])[0])

                    # insurance information
                    patients.setInsuranceCarrier((self.setData("insurance_carrier")[i])[0])
                    patients.setInsuranceAccountNumber((self.setData("insurance_account_number")[i])[0])
                    patients.setInsuranceGroupNumber((self.setData("insurance_group_number")[i])[0])

                    # billing info
                    names = (self.setData("billing_items_name")[i][0]).split('\n')
                    amounts = (self.setData("billing_items_amount")[i][0]).split('\n')

                    if len(names) != 0 and len(amounts) != 0:
                        for j in range(len(names)):
                            amounts[j] = float(amounts[j])
                            patients.addCharge(names[j], amounts[j])

                    patients.setAmountOwed(float((self.setData("amount_owed")[i])[0]))
                    patients.setAmountPaid(float((self.setData("amount_paid")[i])[0]))
                    patients.setAmountPaidByInsurance(float((self.setData("paid_by_insurance")[i])[0]))

                # information that only doctors and nurses may view
                if userType == 0 or userType == 1:

                    # admission info

                    patients.setDateAdmittance((self.setData("date_of_admittance")[i][0]))
                    patients.setTimeAdmittance((self.setData("time_of_admittance")[i][0]))
                    patients.setReasonAdmission((self.setData("reason_for_admission")[i][0]))

                    # discharge info

                    patients.setFamilyDoctor((self.setData("family_doctor")[i][0]))
                    patients.dateDischarge = ((self.setData("discharge_date")[i])[0])
                    patients.timeDischarge = ((self.setData("discharge_time")[i])[0])

                    # treatment notes

                    doctorNotes = (self.setData("doctor_treatment_notes")[i][0]).split('\n')
                    nurseNotes = (self.setData("nurse_treatment_notes")[i][0]).split('\n')

                    if len(doctorNotes) != 0:
                        for note in range(len(doctorNotes)):
                            patients.addDoctorNote(doctorNotes[note])

                    if len(nurseNotes) != 0:
                        for note in range(len(nurseNotes)):
                            patients.addNurseNote(nurseNotes[note])

                    # prescription info

                    prescriptionName = (self.setData("prescription_name")[i][0]).split('\n')
                    prescriptionAmounts = (self.setData("prescription_amount")[i][0]).split('\n')
                    prescriptionTime = (self.setData("prescription_schedule")[i][0]).split('\n')

                    if len(prescriptionName) != 0 and len(prescriptionAmounts) != 0 and len(prescriptionTime) != 0:
                        for j in range(len(prescriptionName)):
                            patients.addPrescription(prescriptionName[j], prescriptionAmounts[j], prescriptionTime[j])

                    # schedules procedures info

                    procedures = (self.setData("scheduled_procedures")[i][0]).split(', ')

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
