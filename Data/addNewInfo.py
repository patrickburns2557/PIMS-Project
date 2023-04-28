from Data.sqlConnector import *
from Data.dataClasses import *

class addNewInfo():

    def __init__(self):

        self.db = myConnector()

    def updatePatient(self, patient, new):

        if new == True:
            self.ID = self.db.checkRowCount()
            # add row for patient if new
            self.db.execute("INSERT into patients (patient_ID) VALUES (" + str(self.ID) + ")")
            # else, get id of patient being updated
        else:
            self.ID = self.db.getID("patient_ID", patient.ID)

        # update personal info
        self.db.update("first_name", patient.firstName, self.ID)
        self.db.update("middle_name", patient.middleName, self.ID)
        self.db.update("last_name", patient.lastName, self.ID)

        self.db.update("address_street", patient.address[0], self.ID)
        self.db.update("address_city", patient.address[1], self.ID)
        self.db.update("address_state", patient.address[2], self.ID)
        self.db.update("address_zip", patient.address[3], self.ID)

        self.db.update("home_phone", patient.homePhone, self.ID)
        self.db.update("work_phone", patient.workPhone, self.ID)
        self.db.update("mobile_phone", patient.mobilePhone, self.ID)

        if len(patient.emergencyContactNames) != 0 and len(patient.emergencyContactNumbers) != 0:
            self.db.update("emergency1_name", patient.emergencyContactNames[0], self.ID)
            self.db.update("emergency1_number", patient.emergencyContactNumbers[0], self.ID)

        if len(patient.emergencyContactNames) >= 2 and len(patient.emergencyContactNumbers) >= 2:
            self.db.update("emergency2_name", patient.emergencyContactNames[1], self.ID)
            self.db.update("emergency2_number", patient.emergencyContactNumbers[1], self.ID)

        if len(patient.emergencyContactNames) >= 3 and len(patient.emergencyContactNumbers) >= 3:
            self.db.update("emergency3_name", patient.emergencyContactNames[2], self.ID)
            self.db.update("emergency3_number", patient.emergencyContactNumbers[2], self.ID)

        # update location info

        self.db.update("facility_name", patient.location[0], self.ID)
        self.db.update("floor_number", patient.location[1], self.ID)
        self.db.update("room_number", patient.location[2], self.ID)
        self.db.update("bed_number", patient.location[3], self.ID)

        self.db.update("allowed_visitor_amount", patient.numAllowedVisitors, self.ID)

        self.visitors = patient.allowedVisitors
        self.visitorString = ""
        for i in range (len(self.visitors)):
            if i != 0:
                self.visitorString += "\n"
            self.visitorString = self.visitorString + self.visitors[i]

        self.db.update("allowed_visitor_names", self.visitorString, self.ID)

        self.db.update("insurance_carrier", patient.insuranceCarrier, self.ID)
        self.db.update("insurance_account_number", patient.insuranceAccountNumber, self.ID)
        self.db.update("insurance_group_number", patient.insuranceGroupNumber, self.ID)

        # update billing info

        self.chargeNames = patient.listCharges
        self.nameString = ""
        for i in range (len(self.chargeNames)):
            if i != 0:
                self.nameString += "\n"
            self.nameString = self.nameString + self.chargeNames[i]

        self.db.update("billing_items_name", self.nameString, self.ID)
        
        self.chargeAmounts = patient.listChargesAmount
        self.amountString = ""
        for i in range (len(self.chargeAmounts)):
            if i != 0:
                self.amountString += "\n"
            amounts = str(self.chargeAmounts[i])
            self.amountString = self.amountString + amounts

        self.db.update("billing_items_amount", self.amountString, self.ID)

        self.db.update("amount_owed", patient.amountOwed, self.ID)
        self.db.update("amount_paid", patient.amountPaid, self.ID)
        self.db.update("paid_by_insurance", patient.amountPaidByInsurance, self.ID)

        # only update medical info if new patient is being added
        if new == True:

            self.db.update("date_of_admittance", patient.dateAdmittance, self.ID)
            self.db.update("time_of_admittance", patient.timeAdmittance, self.ID)
            self.db.update("reason_for_admission", patient.reasonAdmission, self.ID)

            self.db.update("family_doctor", patient.familyDoctor, self.ID)
            self.db.update("discharge_date", patient.dateDischarge, self.ID)
            self.db.update("discharge_time", patient.timeDischarge, self.ID)

            self.doctorNotes = patient.doctorNotes
            self.notesString = ""
            for i in range (len(self.doctorNotes)):
                if i != 0:
                    self.notesString += "\n"
                self.notesString = self.notesString + self.doctorNotes[i]

            self.db.update("doctor_treatment_notes", self.notesString, self.ID)

            self.nurseNotes = patient.nurseNotes
            self.notesString = ""
            for i in range (len(self.nurseNotes)):
                if i != 0:
                    self.notesString += "\n"
                self.notesString = self.notesString + self.nurseNotes[i]

            self.db.update("nurse_treatment_notes", self.notesString, self.ID)

            self.prescriptionName = patient.prescriptionNames
            self.nameString = ""
            for i in range (len(self.prescriptionName)):
                if i != 0:
                    self.nameString += "\n"
                self.nameString = self.nameString + self.prescriptionName[i]

            self.db.update("prescription_name", self.nameString, self.ID)

            self.prescriptionAmount = patient.prescriptionAmount
            self.amountString = ""
            for i in range (len(self.prescriptionAmount)):
                if i != 0:
                    self.amountString += "\n"
                self.amountString = self.amountString + self.prescriptionAmount[i]

            self.db.update("prescription_amount", self.amountString, self.ID)

            self.prescriptionSchedule = patient.prescriptionSchedule
            self.scheduleString = ""
            for i in range (len(self.prescriptionSchedule)):
                if i != 0:
                    self.scheduleString += "\n"
                self.scheduleString = self.scheduleString + self.prescriptionSchedule[i]

            self.db.update("prescription_schedule", self.scheduleString, self.ID)

            self.procedures = patient.scheduledProcedures
            self.procedureString = ""
            for i in range (len(self.procedures)):
                if i != 0:
                    self.procedureString += "\n"
                self.procedureString = self.procedureString + self.procedures[i]

            self.db.update("scheduled_procedures", self.procedureString, self.ID)